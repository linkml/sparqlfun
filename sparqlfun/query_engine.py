import importlib
import logging
from dataclasses import dataclass
from enum import Enum, unique
from typing import Dict, Union, List, Any, Optional, Type

import click
import pkg_resources
from SPARQLWrapper import SPARQLWrapper2, SPARQLWrapper
import SPARQLWrapper.SmartWrapper as sw
from jsonasobj2 import JsonObj
from linkml_runtime.dumpers import json_dumper, yaml_dumper, csv_dumper, rdflib_dumper, rdf_dumper
from linkml_runtime.linkml_model import ClassDefinition
from linkml_runtime.loaders import rdflib_loader, json_loader, yaml_loader
from linkml_runtime.utils.formatutils import camelcase
from linkml_runtime.utils.schemaview import SchemaView, ClassDefinitionName
from linkml_runtime.utils.yamlutils import YAMLRoot, as_json_object
from prefixcommons import curie_util
from rdflib import URIRef, Graph, Literal, BNode, RDF
from rdflib.term import Node
from jinja2 import Template
from sparqlfun.config_schema import SystemConfiguration, Endpoint
import re

RE_COMBINE_WHITESPACE = re.compile(r"\s+")

schema_path = pkg_resources.resource_filename(__name__, 'schema/sparqlfun.yaml')
config_path = pkg_resources.resource_filename(__name__, 'config/endpoints.yaml')

LOGLEVEL = {
    0: logging.WARN,
    1: logging.INFO,
    2: logging.DEBUG,
    3: logging.DEBUG
}
PREFIXMAP = Dict[str, str]
IRI = Union[URIRef, str]
LANGSTR = str

SPARQL_STR = str

#@dataclass
#class SparqlEndpoint:
#    url: Optional[str] = None
#    graph: Optional[Graph] = None
#    named_graph_iri: Optional[IRI] = None
#    type_property: IRI = 'rdf:type'

@dataclass
class SparqlQuery:
    """
    Represents a SPARQL query, which is the query string plus type
    """
    query: SPARQL_STR
    query_type: str = None

    @property
    def normalized_query(self):
        """
        :return: whitespace-normalized version of query
        """
        return RE_COMBINE_WHITESPACE.sub(" ", self.query).strip()


@dataclass
class SparqlTemplateInstance:
    """
    A SPARQL template with some of the parameters bound to concrete values
    """
    query: SparqlQuery = None
    bindings: Dict[str, Any] = None
    python_class: Type[YAMLRoot] = None
    linkml_class: ClassDefinition = None


@dataclass
class SparqlEngine:

    endpoint: Union[str, Endpoint]
    schema_view: SchemaView = SchemaView(schema_path)
    config: SystemConfiguration = None
    lang: LANGSTR = None
    prefix_map: PREFIXMAP = None
    limit: int = 30

    def query(self, template: Union[Type[YAMLRoot], YAMLRoot],
              _url = None,
              **kwargs):
        """

        :param template:
        :param _url:
        :param kwargs:
        :return:
        """

        #graph: Graph = None
        if _url is None:
            _url = self.get_endpoint().url
        prefix_map = self._get_prefix_map()
        cn = template.class_name
        c = self.schema_view.get_class(cn)
        default_vals = self._get_defaults(c)
        ti = self.extract_template_instance(template, **kwargs)
        sq = ti.query
        #sq = self.extract_sparql(template, **kwargs)

        if sq.query_type == 'SELECT':
            spw = SPARQLWrapper2(_url)
            spw.setQuery(sq.query)
            def getval(v: sw.Value) -> Any:
                if v.type == sw.Value.URI:
                    uri = str(v.value)
                    for pfx, uribase in prefix_map.items():
                        if uri.startswith(uribase):
                            return f'{pfx}:{uri.replace(uribase, "")}'
                    return v.value
                else:
                    return v.value
            for result in spw.query().bindings:
                # TODO: default values
                row = {k: getval(v) for k, v in result.items()}
                yield template(**{**row, **kwargs, **default_vals})
        else:
            spw = SPARQLWrapper(_url)
            spw.setQuery(sq.query)
            spw.setReturnFormat(RDF)
            g = spw.query().convert()
            g: Graph
            logging.info(f'Nodes = {len(g.all_nodes())}')
            #for s,p,o in g.triples((None,None,None)):
            #    logging.debug(f' T {s} {p} {o}')
            results_slot_av = c.annotations.get('sparql.results_slot', None)
            if results_slot_av:
                results_slot = self.schema_view.induced_slot(results_slot_av.value, cn)
                results_slot_range = camelcase(results_slot.range)
                logging.info(f'result_slot {results_slot.name}, range = {results_slot_range}')
                module_name = template.__module__
                logging.info(f'M={module_name}')
                module = importlib.import_module(module_name)
                logging.info(f'M={module}')
                result_template = getattr(module, results_slot_range)
            else:
                result_template = template
            logging.info(f'Result template: {result_template}')
            for obj in rdflib_loader.from_rdf_graph(g, target_class=result_template, schemaview=self.schema_view, prefix_map=prefix_map):
                yield obj

    def extract_template_instance(self, template: Union[Type[YAMLRoot], YAMLRoot], **kwargs) -> SparqlTemplateInstance:
        if isinstance(template, YAMLRoot):
            template_py_class = type(template)
            bindings = {}
            for k, v in vars(template).items():
                if v is not None:
                    bindings[k] = v
        else:
            template_py_class = template
            bindings = kwargs
        cn = template_py_class.class_name
        c = self.schema_view.get_class(cn)
        query = self.extract_sparql(template_py_class, **bindings)
        ti = SparqlTemplateInstance(query=query,
                                    bindings=bindings,
                                    python_class=template_py_class,
                                    linkml_class=c)
        return ti

    def extract_sparql_template(self, template: Type[YAMLRoot]) -> SparqlQuery:
        """
        Extract SPARQL from a template class or a prototypical instance

        :param template:
        :param kwargs:
        :return:
        """
        cn = template.class_name
        c = self.schema_view.get_class(cn)
        select_template = self._get_query_template(c, 'sparql.select')
        construct_template = self._get_query_template(c, 'sparql.construct')
        if select_template and construct_template:
            raise Exception(f'Cannot have both select and construct: {template}')
        if not(select_template or construct_template):
            raise Exception(f'Must have EITHER select OR construct: {template}')

        if select_template:
            return SparqlQuery(select_template, 'SELECT')
        else:
            return SparqlQuery(construct_template, 'CONSTRUCT')

    def extract_sparql(self, template: Type[YAMLRoot], **kwargs) -> SparqlQuery:
        """
        Extract SPARQL from a template class or a prototypical instance

        :param template:
        :param kwargs:
        :return:
        """
        sq = self.extract_sparql_template(template)
        # pass-through Jinja2 template rendering
        jt = Template(sq.query)
        query = jt.render(**kwargs)
        # post-Jinja2, replace any variables that are set
        query = self._replace(query, kwargs)
        pfx = self._get_prefix_block(query)
        query = f'{pfx}\n{query}'
        query = f'{query} LIMIT {self.limit}'
        logging.info(f'QUERY={query}')
        return SparqlQuery(query, query_type=sq.query_type)

    def get_config(self):
        if self.config is None:
            self.config = yaml_loader.load(config_path, target_class=SystemConfiguration)
            logging.info(f'CONFIG={self.config}')
        return self.config

    def get_endpoint(self):
        if isinstance(self.endpoint, str):
            logging.info(f'Setting endpoint using name {self.endpoint}')
            self.endpoint = self.get_config().endpoints[self.endpoint]
        return self.endpoint

    def _get_query_template(self, cls: ClassDefinition, kind='sparql.select') -> str:
        q = cls.annotations.get(kind, None)
        if q is not None:
            return q.value
        for rule in cls.classification_rules:
            if not rule.is_a:
                continue
            q = self._get_query_template(self.schema_view.get_class(rule.is_a), kind=kind)
            if q is None:
                return None
            d = {}
            for sn, cond in rule.slot_conditions.items():
                if cond.equals_string is not None:
                    d[sn] = cond.equals_string
            nq = self._replace(q, d)
            return nq
        return None

    def _get_prefix_block(self, query: str = None) -> str:
        lines = []
        for k, v in self._get_prefix_map().items():
            # only include prefixes necessary
            if query is None or f'{k}:' in query:
                lines.append(f'PREFIX {k}: <{v}>')
        return '\n'.join(lines)

    def _get_prefix_map(self) -> PREFIXMAP:
        """
        gets the prefix map, initializing from schema if not already set
        :return: prefix map (mutable)
        """
        # TODO: fix bug where this is necessary
        self.schema_view.imports_closure()
        if self.prefix_map is None:
            self.prefix_map = {k: str(v) for k, v in self.schema_view.namespaces().items()}
        return self.prefix_map

    def bind_prefixes(self, **kwargs):
        pm = self._get_prefix_map()
        for k, v in kwargs.items():
            pm[k] = v
            logging.info(f'Bound {k}: {v}')

    # consider moving to schema_view
    def _get_defaults(self, cls: ClassDefinition) -> Dict:
        d = {}
        for rule in cls.classification_rules:
            for sn, cond in rule.slot_conditions.items():
                if cond.equals_string is not None:
                    d[sn] = cond.equals_string
        for slot in self.schema_view.class_induced_slots(cls.name):
            if slot.equals_string is not None:
                d[slot.name] = d[sn]
        return d

    def _get_namespace_manager(self):
        g = Graph()
        nm = g.namespace_manager
        for k, v in self.schema_view.schema.prefixes.items():
            nm.bind(k, v.prefix_reference)
        return nm


    def _replace(self, template: str, argdict: dict = {}) -> str:
        for k, v in argdict.items():
            template = template.replace(f'?{k}', v)
        return template


def _unwrap(v: sw.Value) -> Node:
    if v.type == sw.Value.URI:
        return URIRef(v.value)
    elif v.type == sw.Value.Literal:
        if v.lang is not None:
            return Literal(v.value, lang=v.lang)
        else:
            return Literal(v.value)
    elif v.type == sw.Value.TypedLiteral:
        return Literal(v.value, datatype=v.datatype)
    elif v.type == sw.Value.BNODE:
        return BNode(v.value)
    else:
        raise Exception(f'Unknown type {v.type} for {v}')

@unique
class OutputFormat(Enum):
    json = 'json'
    yaml = 'yaml'
    tsv = 'tsv'
    ttl = 'ttl'
    obj = 'obj'
    @staticmethod
    def list():
        return list(map(lambda c: c.value, OutputFormat))

@click.command()
@click.option('--endpoint', '-e', help='Name or path of endpoint', required=True)
@click.option('-f', '--to_format', default='json',
              type=click.Choice(OutputFormat.list()),
              help='output format')
@click.option('-l', '--limit', default=10, show_default=True,
              help="limit on number of query results")
@click.option('-M', '--curie-maps', default=['obo_context'],
              show_default=True, multiple=True,
              help="names of CURIE maps to load")
@click.option('-T', '--template',
              required=True,
              help='name of template')
@click.option('-v', '--verbose', count=True)
@click.argument('params', nargs=-1)
def cli(params: List[str], endpoint: str, limit: int, curie_maps: List[str],
        to_format: str, template: str, verbose: int):
    """
    Query sparql template

    Examples:

    \b
        sparqlfun -t
            $ BAR

    """
    logging.basicConfig(level=LOGLEVEL[verbose])
    se = SparqlEngine(endpoint=endpoint)
    sv = se.schema_view

    se.limit = limit
    module = importlib.import_module('sparqlfun.model')
    template_py = getattr(module, template)
    args = []
    kwargs = {}
    prefixes = []
    def add_prefix(curie: str):
        if ':' in curie:
            prefixes.append(curie.split(':')[0])
    for p in params:
        if '=' in p:
            [k, v] = p.split('=')
            kwargs[k] = v
            add_prefix(v)
        else:
            args.append(p)
            add_prefix(p)
    logging.info(f'Prefixes detected in query: {prefixes}')
    for cmap_name in curie_maps:
        cmap = curie_util.read_biocontext(cmap_name)
        for p in prefixes:
            if p in cmap:
                se.bind_prefixes(**{p: cmap[p]})
    if to_format == 'json':
        dumper = json_dumper
    elif to_format == 'yaml':
        dumper = yaml_dumper
    elif to_format == 'tsv':
        dumper = csv_dumper
    elif to_format == 'ttl':
        dumper = rdflib_dumper
    elif to_format == 'jsonld':
        dumper = rdf_dumper
    else:
        raise Exception(f'Unknown format: {to_format}')

    objs = list(se.query(template_py, *args, **kwargs))
    result_set_py_class = getattr(module, 'ResultSet')
    container = result_set_py_class()
    container.results = objs
    if to_format == 'tsv':
        dump_str = csv_dumper.dumps(container, index_slot='results', schemaview=se.schema_view)
    elif to_format == 'ttl':
        dump_str = dumper.dumps(container, schemaview=se.schema_view)
    else:
        dump_str = dumper.dumps(container)
    print(dump_str)


if __name__ == '__main__':
    cli()



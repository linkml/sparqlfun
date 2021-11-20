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
from linkml_runtime.utils.schemaview import SchemaView, ClassDefinitionName
from linkml_runtime.utils.yamlutils import YAMLRoot, as_json_object
from prefixcommons import curie_util
from rdflib import URIRef, Graph, Literal, BNode, RDF
from rdflib.term import Node
from jinja2 import Template
from sparqlfun.config_schema import SystemConfiguration

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

@dataclass
class SparqlEndpoint(object):
    url: Optional[str] = None
    graph: Optional[Graph] = None
    named_graph_iri: Optional[IRI] = None
    type_property: IRI = 'rdf:type'

@dataclass
class SparqlEngine:

    endpoint: SparqlEndpoint
    schema_view: SchemaView = SchemaView(schema_path)
    config: SystemConfiguration = None
    lang: LANGSTR = None
    prefix_map: PREFIXMAP = None
    limit: int = 30

    def query(self, template: YAMLRoot,
              _url = None,
              **kwargs):

        if _url is None:
            _url = self.get_endpoint().url
        prefix_map = self._get_prefix_map()
        cn = template.class_name
        c = self.schema_view.get_class(cn)
        default_vals = self._get_defaults(c)
        select_template = self._get_query_template(c, 'sparql.select')
        construct_template = self._get_query_template(c, 'sparql.construct')
        if select_template and construct_template:
            raise Exception(f'Cannot have both select and construct: {template}')
        if select_template or construct_template:
            if select_template:
                t = select_template
            else:
                t = construct_template
            #query = t.format(**kwargs)
            jt = Template(t)
            query = jt.render(**kwargs)
            query = self._replace(query, kwargs)
            pfx = self._get_prefix_block()
            query = f'{pfx}\n{query}'
            query = f'{query} LIMIT {self.limit}'
            logging.info(f'QUERY={query}')
            if select_template:
                spw = SPARQLWrapper2(_url)
                spw.setQuery(query)
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
                    # TODO: contract URI
                    # TODO: default values
                    row = {k: getval(v) for k, v in result.items()}
                    yield template(**{**row, **kwargs, **default_vals})
            else:
                spw = SPARQLWrapper(_url)
                spw.setQuery(query)
                spw.setReturnFormat(RDF)
                g = spw.query().convert()
                for obj in rdflib_loader.from_rdf_graph(g, target_class=template, schemaview=self.schema_view, prefix_map=prefix_map):
                    yield obj

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

    def _get_prefix_block(self) -> str:
        lines = []
        for k, v in self._get_prefix_map().items():
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

    def _get_defaults(self, cls: ClassDefinition) -> Dict:
        d = {}
        for rule in cls.classification_rules:
            for sn, cond in rule.slot_conditions.items():
                if cond.equals_string is not None:
                    d[sn] = cond.equals_string
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



import importlib
import logging
from dataclasses import dataclass
from enum import Enum, unique
from typing import Dict, Union, List, Any, Optional, Type
import requests

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
from sparqlfun.resultset import ResultSet
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
    """
    Engine that can interpret and executed templated sparql queries
    """

    endpoint: Union[str, Endpoint] = None
    schema_view: SchemaView = SchemaView(schema_path)
    config: SystemConfiguration = None
    lang: LANGSTR = None
    prefix_map: PREFIXMAP = None
    limit: int = 30
    ignore_unmapped_predicates = False

    def query(self, template: Union[Type[YAMLRoot], YAMLRoot, SparqlTemplateInstance],
              _url = None,
              **kwargs) -> ResultSet:
        """
        Compile a template, binding variables, executed, and translate results to objects

        :param template:
        :param _url: uses endpoint URL if not specified
        :param kwargs:
        :return: result set container
        """
        if _url is None:
            _url = self.get_endpoint().url
        logging.info(f'Querying: {_url}')
        prefix_map = self._get_prefix_map()
        cn = template.class_name
        c = self.schema_view.get_class(cn)
        default_vals = self._get_defaults(c)
        if isinstance(template, SparqlTemplateInstance):
            ti = template
        else:
            ti = self.extract_template_instance(template, **kwargs)
        template_py_class = ti.python_class
        sq = ti.query
        logging.info(f'Yasgui: {self.yasgui_url(ti)}')
        for k, v in ti.bindings.items():
            default_vals[k] = v

        objs = []
        result_set = ResultSet()
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
                objs.append(template_py_class(**{**default_vals, **kwargs, **row}))
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
                result_template = template_py_class
            logging.info(f'Result template: {result_template}')
            for obj in rdflib_loader.from_rdf_graph(g, target_class=result_template, schemaview=self.schema_view, prefix_map=prefix_map,
                                                    cast_literals=True,
                                                    ignore_unmapped_predicates=self.ignore_unmapped_predicates):
                objs.append(obj)
        logging.info(f'Num objects = {len(objs)}')
        result_set.results = objs
        return result_set

    def construct(self, template: str,
              _url = None,
              **kwargs) -> Graph:
        if _url is None:
            _url = self.get_endpoint().url
        logging.info(f'Querying: {_url}')
        prefix_map = self._get_prefix_map()
        # TODO: quote literals
        ti = SparqlTemplateInstance(query=SparqlQuery(template),
                                    bindings=kwargs,
                                    linkml_class=self.schema_view.get_class(template))

        default_vals = self._get_defaults(c)
        sq = ti.query
        #for k, v in ti.bindings.items():
        #    default_vals[k] = v

        spw = SPARQLWrapper(_url)
        spw.setQuery(sq.query)
        spw.setReturnFormat(RDF)
        g = spw.query().convert()
        return g

    def yasgui_url(self, template: Union[Type[YAMLRoot], YAMLRoot, SparqlTemplateInstance],
                   _url = None,
                   **kwargs) -> str:
        if _url is None:
            _url = self.get_endpoint().url
        logging.info(f'Querying: {_url}')
        prefix_map = self._get_prefix_map()
        ti = self.extract_template_instance(template, **kwargs)
        params = {
            'query': requests.utils.quote(ti.query.query),
            'endpoint': requests.utils.quote(_url),
        }
        params_str = '&'.join([f'{k}={v}' for k, v in params.items()])
        return f'https://yasgui.triply.cc/#{params_str}'


    def extract_template_instance(self, template: Union[Type[YAMLRoot], YAMLRoot, SparqlTemplateInstance], **kwargs) -> SparqlTemplateInstance:
        """

        :param template:
        :param kwargs:
        :return:
        """
        sv = self.schema_view
        if isinstance(template, SparqlTemplateInstance):
            if len(kwargs.items()):
                logging.error(f'Ignoring kwargs: {kwargs}, as template already instantiated: {template}')
            return template
        if isinstance(template, YAMLRoot):
            template_py_class = type(template)
            bindings = {}
            for k, v in vars(template).items():
                # only use values that have been set
                if v is not None and not isinstance(v, list) and not isinstance(v, dict):
                    bindings[k] = v
        else:
            template_py_class = template
            bindings = kwargs
        cn = template_py_class.class_name
        c = sv.get_class(cn)
        for k, v in bindings.items():
            slot = sv.induced_slot(k, cn)
            if slot.range in sv.all_types():
                t = sv.get_type(slot.range)
                if t.base == 'str':
                    v = f'"{v}"'
            bindings[k] = v
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
        query = jt.render(_values=lambda l: ' '.join(l),
                          **kwargs)
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
        import re
        m = re.search(r'(.*\s+where\s*\{)(\s+.*)', template, flags=re.IGNORECASE | re.DOTALL)
        if m:
            in_select = m.group(1)
            post_select = m.group(2)
        else:
            raise ValueError(f'No WHERE in query: {template}')
        template = in_select
        sv = self.schema_view
        #def serialize(k: str, v: str):

        for k, v in argdict.items():
            if isinstance(v, list):
                v = ' '.join(v)
            template += f'\n  VALUES ?{k} {{ {v} }} .'
        template += post_select
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






import importlib
import logging
from dataclasses import dataclass
from enum import Enum, unique
from typing import Dict, Union, List, Any, Optional, Type
import requests

import click
from linkml_runtime.dumpers import json_dumper, yaml_dumper, csv_dumper, rdflib_dumper, rdf_dumper
from linkml_runtime.utils.schemaview import SchemaView, ClassDefinitionName
from linkml_runtime.utils.yamlutils import YAMLRoot, as_json_object
from prefixcommons import curie_util
from rdflib import URIRef, Graph, Literal, BNode, RDF
from rdflib.term import Node
from jinja2 import Template

import sparqlfun
from sparqlfun import SparqlEngine
from sparqlfun.config_schema import ExampleQuery


def example_query_to_cli(ex: ExampleQuery, endpoint: str) -> str:
    bindings = ' '.join([f'{k}={v.binding_value}' for k, v in ex.bindings.items()])
    return f'sparqlfun query -e {endpoint} -T {ex.query_template} {bindings}'

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

@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
def main(verbose: int, quiet: bool):
    """Run the SPARQLFUN CLI."""
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    if quiet:
        logging.basicConfig(level=logging.ERROR)





@main.command()
@click.option('--endpoint', '-e',
              help='Name or path of endpoint', required=True)
@click.option('-f', '--to_format', default='json',
              type=click.Choice(OutputFormat.list()),
              help='output format')
@click.option('-l', '--limit', default=10, show_default=True,
              help="limit on number of query results")
@click.option('-M', '--curie-maps', default=['obo_context'],
              show_default=True, multiple=True,
              help="names of CURIE maps to load")
@click.option('-P', '--prefix',
              multiple=True,
              help="prefix list, specified as prefix=uribase")
@click.option('-m', '--module', default='sparqlfun.model',
              show_default=True,
              help="name of module to load")
@click.option('-S', '--schema',
              help="path to schema, if not default")
@click.option('--yasgui/--no-yasgui', default=False, show_default=True,
              help="return URL to yasgui interface rather than execute query")
@click.option('-T', '--template',
              required=True,
              help='name of template')
@click.argument('params', nargs=-1)
def query(params: List[str], module: str, schema: str, endpoint: str, limit: int, curie_maps: List[str], prefix: List[str],
          yasgui, to_format: str, template: str,):
    """
    Query sparql template

    \b
    Examples:

    \b
        common ancestors

            $ sparqlfun query -e ubergraph -T PairwiseCommonSubClassAncestor node1=GO:0046220 node2=GO:0008295

    """
    se = SparqlEngine(endpoint=endpoint)
    logging.info(f'Engine={se}')
    se.ignore_unmapped_predicates = True
    if schema:
        se.schema_view = SchemaView(schema)
    sv = se.schema_view

    se.limit = limit
    module = importlib.import_module(module)
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
            if ',' in v:
                # TODO: allow escape mechanism if a comma is to be included
                v = v.split(',')
                for x in v:
                    add_prefix(x)
            else:
                add_prefix(v)
            if ',' in k:
                for k1 in k.split(','):
                    kwargs[k1] = v
            else:
                kwargs[k] = v
        else:
            args.append(p)
            add_prefix(p)
    logging.info(f'Prefixes detected in query: {prefixes}')
    for cmap_name in curie_maps:
        cmap = curie_util.read_biocontext(cmap_name)
        for p in prefixes:
            if p in cmap:
                se.bind_prefixes(**{p: cmap[p]})
    for p in prefix:
        [k,v] = p.split('=')
        se.bind_prefixes(**{k: v})
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

    if yasgui:
        yasgui_url = se.yasgui_url(template_py, **kwargs)
        print(yasgui_url)
        exit(0)

    container = se.query(template_py, *args, **kwargs)
    #result_set_py_class = getattr(module, 'ResultSet')
    #container = result_set_py_class()
    #container.results = objs
    if to_format == 'tsv':
        dump_str = csv_dumper.dumps(container, index_slot='results', schemaview=se.schema_view)
    elif to_format == 'ttl':
        dump_str = dumper.dumps(container, schemaview=se.schema_view)
    else:
        dump_str = dumper.dumps(container)
    print(dump_str)


@main.command()
@click.option('-D', '--detail/--no-detail',
              default=False, show_default=True,
              help="Show detailed info on each template")
def endpoints(detail):
    """
    List all endpoints
    """
    se = SparqlEngine()
    print('# Sparqlfun Endpoints\n')
    cfg = se.get_config()
    for en, e in cfg.endpoints.items():
        if detail:
            print(f'\n## Endpoint: {en}\n')
            if e.description:
                print(f'_{e.description}_\n')
            print(f'* URL: {e.url}')
            print(f'* Implements Profiles:')
            for imp in e.implements:
                profile = cfg.profiles[imp]
                print(f'    * {imp}: {profile.description}')
            if e.example_queries:
                print('\n### EXAMPLES\n')
                for ex in e.example_queries:
                    print(f'\n#### {ex.query_template}\n')
                    print(f'{ex.description}\n')
                    cmd = example_query_to_cli(ex, en)
                    print(f'```')
                    print(cmd)
                    print(f'```')
        else:
            print(f'* {en}: {e.description}')


@main.command()
@click.option('--endpoint', '-e',
              help='Name or path of endpoint', required=False)
@click.option('--module', '-m',
              help="name of module")
@click.option('-D', '--detail/--no-detail',
              default=False, show_default=True,
              help="Show detailed info on each template")
@click.argument('matches', nargs=-1)
def templates(matches, endpoint, module, detail):
    """
    List all templates
    """
    print('# TEMPLATES\n')
    #sv = package_schemaview("sparqlfun")
    sv = SchemaView(sparqlfun.query_engine.schema_path)
    mmap = {}
    for m in sv.imports_closure(True):
        module_schema = sv.schema_map[m]
        mmap[module_schema.default_prefix] = module_schema.id
    for cn, c in sv.all_classes().items():
        this_mod = c.from_schema
        include = True
        if module:
            include = module == this_mod or mmap.get(this_mod, Node) == module or mmap.get(module, None) == this_mod
            logging.debug(f'Testing: {cn} module, include={include}')
        if not include:
            continue
        if matches:
            if not any(m.lower() in cn.lower() for m in matches):
                logging.debug(f'Skipping: {cn} Could not find any of the matches: {matches}')
                continue
        if detail:
            print(f'\n## {cn}\n')
            print(f'* Desc: {c.description}')
            print(f'* Module: {this_mod}')
            print(f'\n### Slots\n')
            for s in sv.class_induced_slots(cn):
                print(f'* {s.name}: {s.range}')
        else:
            print(f'* {cn} ({this_mod}): {c.description}')


if __name__ == '__main__':
    main()

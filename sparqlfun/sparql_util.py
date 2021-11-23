"""
Provides single abstraction layer for SPARQL over in-memory rdflib objects and remote triplestores
"""
from typing import Dict

from SPARQLWrapper import SPARQLWrapper2, RDF
from rdflib import Graph, Literal, URIRef, BNode
import SPARQLWrapper.SmartWrapper as sw
from rdflib.term import Node


def sparql_select(query: str, url: str = None, graph: Graph = None):
    """
    SPARQL SELECT over in-memory graph or remote endpoint

    :param query: SPARQL query (required)
    :param url: endpoint URL (required for remote)
    :param graph: in-memory graph (required for local)
    :return:
    """
    if graph is not None:
        print(f'GRAPH={graph}')
        for row in graph.query(query):
            print(f'ROW={row}')
            yield row
    else:
        if url is None:
            raise ValueError(f'Must specify EITHER url OR graph')

        spw = SPARQLWrapper2(url)
        spw.setQuery(query)
        for result in sw.query().bindings:
            row = {k: convert_sparql_value(v) for k, v in result.items()}
            yield row

def sparql_construct(query: str, url: str = None, graph: Graph = None) -> Graph:
    """
    SPARQL CONSTRUCT over in-memory graph or remote endpoint

    :param query: SPARQL query (required)
    :param url: endpoint URL (required for remote)
    :param graph: in-memory graph (required for local)
    """
    if graph is not None:
        return_graph = Graph()
        for row in graph.query(sparql):
            graph.add(row)
        return return_graph
    else:
        if url is None:
            raise ValueError(f'Must specify EITHER url OR graph')
        spw = SPARQLWrapper(url)
        spw.setQuery(query)
        spw.setReturnFormat(RDF)
        return spw.query().convert()

def convert_sparql_value(v: sw.Value) -> Node:
    """
    Converts values returned by SPARQLWrapper2

    :param v:
    :return:
    """
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
import os
import pytest

from sparqlfun import SparqlEngine
from sparqlfun.model import NodeObject, Triple, DefinitionTriple
from tests import INPUT_DIR, check, NUCLEUS, GO_TEST_TTL
from rdflib import Graph, ConjunctiveGraph


@pytest.fixture(autouse=True)
def engine():
    g = ConjunctiveGraph()
    g.parse(GO_TEST_TTL, format='ttl')
    se = SparqlEngine(endpoint=g)
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/',
                     NCBITaxon='http://purl.obolibrary.org/obo/NCBITaxon_',
                     BFO='http://purl.obolibrary.org/obo/BFO_',
                     UBERON='http://purl.obolibrary.org/obo/UBERON_')
    return se


def test_triples(engine):
    engine.limit = 1000
    check(engine.query(Triple, subject=[NUCLEUS]),
          min_expected=5,
          must_contain=[Triple(subject=NUCLEUS, predicate='rdfs:subClassOf', object='GO:0043231')],
          outfile='Local-Triple-go-nucleus.yaml')


def test_classification(engine):
    engine.limit = 1000
    check(engine.query(DefinitionTriple, subject=[NUCLEUS]),
          min_expected=1,
          max_expected=1,
          outfile='Local-DefinitionTriple-go-nucleus.yaml')

def test_conjunctive_graph(engine):
    engine.limit = 1000
    check(engine.query(NodeObject, id=[NUCLEUS]),
          min_expected=1,
          max_expected=1,
          outfile='Local-NodeObject-go-nucleus.yaml')

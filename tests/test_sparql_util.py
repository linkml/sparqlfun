import os
import pytest

from sparqlfun.sparql_util import sparql_select
from tests import INPUT_DIR
from rdflib import Graph

DATA = os.path.join(INPUT_DIR, 'go-nucleus.ttl')

@pytest.fixture
def example_graph():
    g = Graph()
    return g.parse(DATA, format='ttl')

def test_sparql_select_local(example_graph):
    #rows = sparql_select("SELECT * WHERE {?x rdf:type owl:Class}", graph=example_graph)
    rows = sparql_select("SELECT * WHERE {?x ?r ?y}", graph=example_graph)
    for row in rows:
        print(f'ROW={row}')

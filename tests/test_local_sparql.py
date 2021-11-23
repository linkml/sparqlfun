import os
import pytest

from tests import INPUT_DIR
from rdflib import Graph

DATA = os.path.join(INPUT_DIR, 'go-nucleus.ttl')

@pytest.fixture
def example_graph():
    g = Graph()
    return g.parse(DATA, format='ttl')

def test_sparql_select_local(example_graph):
    #rows = sparql_select("SELECT * WHERE {?x rdf:type owl:Class}", graph=example_graph)
    query = "SELECT * WHERE {?x ?r ?y}"
    for row in example_graph.query(query):
        print(f'ROW={row}')

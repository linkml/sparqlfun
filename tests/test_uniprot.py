import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='uniprot')
    se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    return se

def check(rs: ResultSet, min_expected=1, max_expected: int = None):
    n = 0
    for result in rs.results:
        print(f'RESULT={result}')
        n += 1
    assert n >= min_expected
    if max_expected is not None:
        assert n <= max_expected


#def test_protein(engine):
#    check(engine.query(Protein(id='uniprot:Q15465')))
@pytest.mark.skip(reason="compatibility issues between rdflib and uniprot endpoint")
def test_classified_with(engine):
    q = ProteinClassifiedWith(object='GO:0006915')
    check(engine.query(q))
import pytest
import logging

from sparqlfun.gocam_queries import ModelInfo
from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)

BILATERIA = 'NCBITaxon:33213'
PRIMATES = 'NCBITaxon:9443'
INNER_MEMBRANE_PELLICLE_COMPLEX = 'GO:0070258'
PART_OF = 'BFO:0000050'


@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='go')
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/',
                     NCBITaxon='http://purl.obolibrary.org/obo/NCBITaxon_',
                     BFO='http://purl.obolibrary.org/obo/BFO_',
                     GO='http://purl.obolibrary.org/obo/GO_')
    return se

def check(rs: ResultSet, min_expected=1, max_expected: int = None):
    n = 0
    for result in rs.results:
        print(f'RESULT={result}')
        n += 1
    assert n >= min_expected
    if max_expected is not None:
        assert n <= max_expected


#def test_model_query(engine):
#    check(engine.query(ModelInfo, state="production"))
#    check(engine.query(DescribeEquivalentExpression))

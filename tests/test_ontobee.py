import os

import pytest
import logging

from linkml_runtime.dumpers import yaml_dumper

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)

BILATERIA = 'NCBITaxon:33213'
PRIMATES = 'NCBITaxon:9443'
INNER_MEMBRANE_PELLICLE_COMPLEX = 'GO:0070258'
PART_OF = 'BFO:0000050'

DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(DIR, 'output')


@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='ontobee')
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/',
                     NCBITaxon='http://purl.obolibrary.org/obo/NCBITaxon_',
                     BFO='http://purl.obolibrary.org/obo/BFO_',
                     UBERON='http://purl.obolibrary.org/obo/UBERON_',
                     GO='http://purl.obolibrary.org/obo/GO_')
    return se

def check(rs: ResultSet, min_expected=1, max_expected: int = None, outfile=None):
    n = 0
    for result in rs.results:
        print(f'RESULT={result}')
        n += 1
    assert n >= min_expected
    if max_expected is not None:
        assert n <= max_expected
    if outfile:
        yaml_dumper.dump(rs, to_file=os.path.join(OUTPUT_DIR, outfile))


def test_construct(engine):
    engine.limit = 1000
    check(engine.query(NodeObject, id='UBERON:0002062'),
          outfile='Ontobee-NodeObject-uberon-0002062.yaml')

def test_multivalued(engine):
    engine.limit = 1000
    check(engine.query(NodeObject, id=['UBERON:0002062', 'UBERON:0002061']),
          outfile='Ontobee-NodeObject-uberon-0002061-0002062.yaml')

def test_triple(engine):
    engine.limit = 1000
    check(engine.query(Triple, subject=['UBERON:0002062']),
          outfile='Ontobee-Triple-uberon-0002062.yaml')


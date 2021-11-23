import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)

#@pytest.fixture
#def ubergraph_url():
#    return 'ubergraph'

@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='ubergraph')
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
    return se

def test_limit_zero(engine):
    engine.limit = 0
    assert len(list(engine.query(Triple, subject='GO:0005694'))) == 0

def test_limit_default(engine):
    assert engine.limit > 0
    assert len(list(engine.query(Triple, subject='GO:0005694'))) > 1

def test_limit_one(engine):
    engine.limit = 1
    assert len(list(engine.query(Triple, subject='GO:0005694'))) == 1

def test_ubergraph(engine):
    se = engine
    #se = SparqlEngine(endpoint=ubergraph_url)
    #se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
    print(f'PM={se._get_prefix_map()}')
    print(f'se = {se}')
    for row in se.query(BasicClass, id='GO:0005694'):
        print(f'BC={row}')
    for row in se.query(RdfTypeTriple, object='owl:Class'):
        print(f'ROW={row}')
    print('DONE')
    for row in se.query(Quad, object='owl:ObjectProperty'):
        print(f'ROW={row}')
    for row in se.query(RdfsSubclassOfTriple, object='GO:0005694'):
        print(f'ROW={row}')

def test_nr(engine):
    se = engine
    se.limit = 3
    #se = SparqlEngine(endpoint=ubergraph_url)
    #se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
    for row in se.query(NonRedundantQuad, subject='GO:0005694'):
        print(f'ROW={row}')

def test_taxon(engine):
    for row in engine.query(UbergraphTaxonClass):
        print(f'ROW={row}')

def test_never_in_taxon(engine):
    for row in engine.query(InferredNeverInTaxon, object='NCBITaxon:33213'):
        print(f'ROW={row}')

def test_definition(engine):
    #se = SparqlEngine(endpoint=ubergraph_url)
    #se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    for row in engine.query(DefinitionTriple, subject='GO:0005694'):
        print(f'ROW={row}')

def test_jinja(engine):
    #se = SparqlEngine(endpoint=ubergraph_url)
    #se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    for row in engine.query(OboClassFiltered, query_has_subclass_ancestor='GO:0044271'):
        print(f'ROW={row}')

def test_query(engine):
    engine.limit = 9999
    for row in engine.query(OboClassQuery, label_regex='^cysteine metabol'):
        print(f'ROW={row}')

def test_common_ancestor(engine):
    for row in engine.query(PairwiseCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'):
        print(f'ROW={row}')

def test_namespaces(engine):
    print(f'PM={engine._get_prefix_map()}')
    print(f'SM = {engine.schema_view.schema_map.keys()}')
    pb = engine._get_prefix_block()
    print(pb)
    assert 'renci' in pb

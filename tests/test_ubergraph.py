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

def check(rs: ResultSet, min_expected=1, max_expected: int = None):
    n = 0
    for result in rs.results:
        print(f'RESULT={result}')
        n += 1
    assert n >= min_expected
    if max_expected is not None:
        assert n <= max_expected


def test_limit_zero(engine):
    engine.limit = 0
    assert engine.query(Triple, subject='GO:0005694').results == []

def test_limit_default(engine):
    assert engine.limit > 0
    assert len(engine.query(Triple, subject='GO:0005694').results) > 1

def test_limit_one(engine):
    engine.limit = 1
    assert len(engine.query(Triple, subject='GO:0005694').results) == 1

def test_kwargs_style(engine):
    check(engine.query(BasicClass, id='GO:0005694'))
    check(engine.query(RdfTypeTriple, object='owl:Class'))
    check(engine.query(Quad, object='owl:ObjectProperty'))
    check(engine.query(RdfsSubclassOfTriple, object='GO:0005694'))

def test_proto_style(engine):
    check(engine.query(RdfTypeTriple(object='owl:Class')))
    check(engine.query(Quad(object='owl:ObjectProperty')))
    check(engine.query(RdfsSubclassOfTriple(object='GO:0005694')))
    check(engine.query(BasicClass(id='GO:0005694')))

def test_construct(engine):
    check(engine.query(BasicClass(id='GO:0005694')))

def test_nr(engine):
    check(engine.query(NonRedundantQuad, subject='GO:0005694'))

def test_taxon_class(engine):
    check(engine.query(UbergraphTaxonClass))
    # TODO: if no variables in SELECT then convert to an ASK
    #check(engine.query(UbergraphTaxonClass(id='NCBITaxon:1')))

def test_never_in_taxon(engine):
    check(engine.query(InferredNeverInTaxon(object='NCBITaxon:33213')))

def test_definition(engine):
    check(engine.query(DefinitionTriple, subject='GO:0005694'), max_expected=1)

def test_jinja(engine):
    check(engine.query(OboClassFiltered, query_has_subclass_ancestor='GO:0044271'))

def test_regex(engine):
    check(engine.query(OboClassQuery, label_regex='^cysteine metabol'))

def test_common_ancestor(engine):
    check(engine.query(PairwiseCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'))



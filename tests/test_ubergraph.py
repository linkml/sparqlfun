import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)

BILATERIA = 'NCBITaxon:33213'
PRIMATES = 'NCBITaxon:9443'
INNER_MEMBRANE_PELLICLE_COMPLEX = 'GO:0070258'
PART_OF = 'BFO:0000050'


@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='ubergraph')
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

def test_taxon_exclusion_via_never_in(engine):
    check(engine.query(ClassTaxonExclusionViaNeverIn(object=BILATERIA)))
    check(engine.query(ClassTaxonExclusionViaNeverIn(subject=INNER_MEMBRANE_PELLICLE_COMPLEX,
                                                     predicate=PART_OF,
                                                     object=BILATERIA)))

def test_taxon_exclusion_via_only_in(engine):
    check(engine.query(ClassTaxonExclusionViaOnlyIn(object=BILATERIA)))

def test_taxon_exclusion(engine):
    check(engine.query(ClassTaxonExclusion(object=BILATERIA)))

def test_taxon_exclusion_primates(engine):
    check(engine.query(ClassTaxonExclusion(object=PRIMATES)))

def test_definition(engine):
    check(engine.query(DefinitionTriple, subject='GO:0005694'), max_expected=1)

def test_jinja(engine):
    check(engine.query(OboClassFiltered, query_has_subclass_ancestor='GO:0044271'))

def test_custom_result_set(engine):
    check(engine.query(OboClassQuery, label_regex='^cysteine metabol'))

def test_common_ancestor(engine):
    check(engine.query(PairwiseCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'))

def test_setwise_common_ancestor(engine):
    check(engine.query(SetwiseCommonSubClassAncestor, nodes=['GO:0046220', 'GO:0008295']))

def test_mrca(engine):
    check(engine.query(PairwiseMostRecentCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'))

def test_setwise_mrca(engine):
    check(engine.query(SetwiseMostRecentCommonSubClassAncestor, nodes=['GO:0046220', 'GO:0008295']))

def test_owl(engine):
    check(engine.query(OwlNamedEquivalentClassTriple))
    # TODO: allow blank nodes
    #check(engine.query(SomeValuesFromRestriction, predicate='BFO:0000050'))

def test_relationship(engine):
    check(engine.query(SubclassOfSomeValuesFrom))

# TODO
#def test_describe(engine):
#    engine.ignore_unmapped_predicates = True
#    check(engine.query(DescribeEquivalentExpression))
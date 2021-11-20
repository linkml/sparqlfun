from sparqlfun.query_engine import SparqlEngine, SparqlEndpoint
from sparqlfun.model import *


def test_ubergraph():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
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

def test_nr():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
    for row in se.query(NonRedundantQuad, subject='GO:0005694'):
        print(f'ROW={row}')

def test_taxon():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    for row in se.query(TaxonClass):
        print(f'ROW={row}')

def test_never_in_taxon():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    for row in se.query(InferredNeverInTaxon, object='NCBITaxon:33213'):
        print(f'ROW={row}')

def test_definition():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    for row in se.query(DefinitionTriple, subject='GO:0005694'):
        print(f'ROW={row}')

def test_jinja():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    for row in se.query(OboClassFiltered, query_has_subclass_ancestor='GO:0044271'):
        print(f'ROW={row}')

def test_common_ancestor():
    se = SparqlEngine(endpoint='ubergraph')
    se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    for row in se.query(PairwiseCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'):
        print(f'ROW={row}')

def test_namespaces():
    se = SparqlEngine(endpoint=SparqlEndpoint('https://stars-app.renci.org/ubergraph/sparql'))
    #impc = se.schema_view.imports_closure()
    #print(f'IMP={impc}')
    se.bind_prefixes(hgnc='http://identifiers.org/hgnc/', GO='http://purl.obolibrary.org/obo/GO_')
    print(f'PM={se._get_prefix_map()}')
    print(f'SM = {se.schema_view.schema_map.keys()}')
    pb = se._get_prefix_block()
    print(pb)
    assert 'renci' in pb

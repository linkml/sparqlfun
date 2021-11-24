import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)



@pytest.fixture(autouse=True)
def engine() -> SparqlEngine:
    se = SparqlEngine(endpoint='ubergraph')
    return se

def test_basic_instantiation(engine: SparqlEngine):
    ti = engine.extract_template_instance(RdfTypeTriple, object='owl:Class')
    print(ti)
    assert ti.bindings['object'] == 'owl:Class'
    assert len(ti.bindings.keys()) == 1
    qstr = ti.query.normalized_query
    print(qstr)
    # Assumes a particular canonical serialization
    assert 'SELECT * WHERE { VALUES ?object { owl:Class } . VALUES ?predicate { rdf:type } . ?subject ?predicate ?object}' in qstr
    assert 'LIMIT' in qstr
    assert 'PREFIX owl' in qstr

def test_instantiation_from_prototype(engine: SparqlEngine):
    proto = RdfTypeTriple(object='owl:Class')
    ti = engine.extract_template_instance(proto)
    print(ti)
    assert ti.bindings['object'] == 'owl:Class'
    assert len(ti.bindings.keys()) == 1
    qstr = ti.query.normalized_query
    print(qstr)
    assert 'SELECT * WHERE { VALUES ?object { owl:Class } . VALUES ?predicate { rdf:type } . ?subject ?predicate ?object}' in qstr
    assert 'LIMIT' in qstr
    assert 'PREFIX owl' in qstr

def test_instantiation_from_prototype2(engine: SparqlEngine):
    proto = UbergraphTaxonClass(id='NCBITaxon:1')
    ti = engine.extract_template_instance(proto)
    print(ti)
    assert ti.bindings['id'] == 'NCBITaxon:1'
    assert len(ti.bindings.keys()) == 1
    qstr = ti.query.normalized_query
    print(qstr)
    assert 'PREFIX NCBITaxon' in qstr

def test_instantiation_from_with_list(engine: SparqlEngine):
    proto = BasicClass(id='NCBITaxon:1')
    ti = engine.extract_template_instance(proto)
    print(ti)
    assert ti.bindings['id'] == 'NCBITaxon:1'
    assert len(ti.bindings.keys()) == 1
    qstr = ti.query.normalized_query
    print(qstr)
    assert 'PREFIX NCBITaxon' in qstr

def test_namespaces(engine):
    engine.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    print(f'PM={engine._get_prefix_map()}')
    assert engine._get_prefix_map()["GO"] == 'http://purl.obolibrary.org/obo/GO_'
    schema_map = engine.schema_view.schema_map
    print(f'SM = {schema_map.keys()}')
    assert 'sparqlfun' in schema_map
    assert 'rdf' in schema_map
    pb = engine._get_prefix_block()
    print(pb)
    #assert 'renci' in pb
    assert 'PREFIX GO:' in pb


def test_custom_prefixes(engine: SparqlEngine):
    engine.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
    proto = RdfsSubclassOfTriple(object='GO:0005694')
    ti = engine.extract_template_instance(proto)
    print(ti)
    assert ti.bindings['object'] == 'GO:0005694'
    assert len(ti.bindings.keys()) == 1
    qstr = ti.query.normalized_query
    print(qstr)
    # Assumes a particular canonical serialization
    assert 'SELECT * WHERE { VALUES ?object { GO:0005694 } . VALUES ?predicate { rdfs:subClassOf } . ?subject ?predicate ?object}' in qstr
    assert 'LIMIT' in qstr
    assert 'PREFIX rdfs' in qstr
    assert 'PREFIX GO: <http://purl.obolibrary.org/obo/GO_>' in qstr
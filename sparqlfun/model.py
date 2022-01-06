# Auto generated from sparqlfun.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-08T10:58:47
# Schema: sparqlfun
#
# id: https://linkml.io/sparqlfun
# description: SPARQL Templates
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, Ncname, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RESULTSET = CurieNamespace('resultset', 'https://linkml.io/sparqlfun/resultset')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SPARQLFUN = CurieNamespace('sparqlfun', 'https://linkml.io/sparqlfun/')
SPARQLFUN_BIOLINK = CurieNamespace('sparqlfun_biolink', 'https://linkml.io/sparqlfun/biolink')
SPARQLFUN_OMO = CurieNamespace('sparqlfun_omo', 'https://linkml.io/sparqlfun/omo')
SPARQLFUN_OWL = CurieNamespace('sparqlfun_owl', 'https://linkml.io/sparqlfun/owl')
SPARQLFUN_RDF = CurieNamespace('sparqlfun_rdf', 'https://linkml.io/sparqlfun/rdf/')
SPARQLFUN_UBERGRAPH = CurieNamespace('sparqlfun_ubergraph', 'https://linkml.io/sparqlfun/ubergraph')
UBERGRAPH = CurieNamespace('ubergraph', 'http://reasoner.renci.org/')
UPCORE = CurieNamespace('upcore', 'http://purl.uniprot.org/core/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SPARQLFUN


# Types
class NodeIdType(Uriorcurie):
    """ IDs are either CURIEs, IRI, or blank nodes. IRIs are wrapped in <>s to distinguish them from CURIEs, but in general it is good practice to populate the [prefixes][Prefixes.md] table such that they are shortened to CURIEs. Blank nodes are ids starting with `_:`. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "node id type"
    type_model_uri = SPARQLFUN.NodeIdType


class LiteralAsStringType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "literal as string type"
    type_model_uri = SPARQLFUN.LiteralAsStringType


# Class references
class BindingBindingKey(extended_str):
    pass


class NodeId(NodeIdType):
    pass


class BlankNodeId(NodeId):
    pass


class IriNodeId(NodeId):
    pass


class TypedNodeId(NodeId):
    pass


class ClassNodeId(TypedNodeId):
    pass


class PropertyNodeId(TypedNodeId):
    pass


class NamedIndividualNodeId(NodeId):
    pass


class NodeObjectId(NodeId):
    pass


class NestedNodeObjectId(NodeId):
    pass


class BasicClassId(NodeId):
    pass


class TaxonApplicableClassId(ClassNodeId):
    pass


class TaxonClassId(ClassNodeId):
    pass


class GraphClassNodeId(ClassNodeId):
    pass


class OboClassId(GraphClassNodeId):
    pass


class UbergraphTaxonClassId(TaxonClassId):
    pass


class OboClassFilteredId(ClassNodeId):
    pass


class OboClassWithCategoryId(OboClassId):
    pass


class AnatomicalEntityId(OboClassId):
    pass


class BloodVesselId(OboClassId):
    pass


class CellTypeId(OboClassId):
    pass


class ThingId(NodeIdType):
    pass


class ProteinId(ThingId):
    pass


class SubcellularLocationId(ThingId):
    pass


class DiseaseId(ThingId):
    pass


class ProteinExistenceId(ThingId):
    pass


class OrganelleId(ThingId):
    pass


class FamilyMembershipStatementId(ThingId):
    pass


class ClassId(ThingId):
    pass


class StatementId(ThingId):
    pass


class EnzymeId(ThingId):
    pass


class TaxonId(ThingId):
    pass


class CitationId(ThingId):
    pass


class DomainAssignmentStatementId(StatementId):
    pass


class UnpublishedCitationId(CitationId):
    pass


class OrientationId(SubcellularLocationId):
    pass


class NotObsoleteTaxonId(TaxonId):
    pass


class ObservationCitationId(UnpublishedCitationId):
    pass


class CitationStatementId(StatementId):
    pass


class PartId(ThingId):
    pass


class NotObsoleteProteinId(ProteinId):
    pass


class StructureMappingStatementId(StatementId):
    pass


class ObsoleteTaxonId(TaxonId):
    pass


class ConceptId(ClassId):
    pass


class TopologyId(SubcellularLocationId):
    pass


class ObsoleteProteinId(ProteinId):
    pass


class MemberOfRedudantProteomeId(ObsoleteProteinId):
    pass


class JournalId(ThingId):
    pass


class PublishedCitationId(CitationId):
    pass


class SubmissionCitationId(PublishedCitationId):
    pass


class JournalCitationId(PublishedCitationId):
    pass


class PatentCitationId(PublishedCitationId):
    pass


class BookCitationId(PublishedCitationId):
    pass


class CellularComponentId(SubcellularLocationId):
    pass


class NucleotideMappingStatementId(StatementId):
    pass


class DatabaseId(ClassId):
    pass


class EndpointStatementId(StatementId):
    pass


class ProteomeComponentId(ThingId):
    pass


class ElectronicCitationId(PublishedCitationId):
    pass


class ThesisCitationId(PublishedCitationId):
    pass


class ClusterId(ThingId):
    pass


class GeneId(ConceptId):
    pass


class GenericResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.GenericResult
    class_class_curie: ClassVar[str] = "resultset:GenericResult"
    class_name: ClassVar[str] = "GenericResult"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GenericResult


@dataclass
class ResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.ResultSet
    class_class_curie: ClassVar[str] = "resultset:ResultSet"
    class_name: ClassVar[str] = "ResultSet"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ResultSet

    results: Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, GenericResult) else GenericResult(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)


@dataclass
class Binding(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.Binding
    class_class_curie: ClassVar[str] = "resultset:Binding"
    class_name: ClassVar[str] = "Binding"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Binding

    binding_key: Union[str, BindingBindingKey] = None
    binding_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.binding_key):
            self.MissingRequiredField("binding_key")
        if not isinstance(self.binding_key, BindingBindingKey):
            self.binding_key = BindingBindingKey(self.binding_key)

        if self.binding_value is not None and not isinstance(self.binding_value, str):
            self.binding_value = str(self.binding_value)

        super().__post_init__(**kwargs)


NodeOrLiteral = Any

@dataclass
class Prefix(YAMLRoot):
    """
    Maps CURIEs to URIs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SH.PrefixDeclaration
    class_class_curie: ClassVar[str] = "sh:PrefixDeclaration"
    class_name: ClassVar[str] = "prefix"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Prefix

    prefix: Optional[Union[str, NCName]] = None
    base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.prefix is not None and not isinstance(self.prefix, NCName):
            self.prefix = NCName(self.prefix)

        if self.base is not None and not isinstance(self.base, URI):
            self.base = URI(self.base)

        super().__post_init__(**kwargs)


class NodeTrait(YAMLRoot):
    """
    abstract groupings/properties for different aspects of the model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NodeTrait
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NodeTrait"
    class_name: ClassVar[str] = "node trait"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeTrait


class ClassTrait(NodeTrait):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.ClassTrait
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:ClassTrait"
    class_name: ClassVar[str] = "class trait"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ClassTrait


class PropertyTrait(NodeTrait):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.PropertyTrait
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:PropertyTrait"
    class_name: ClassVar[str] = "property trait"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PropertyTrait


class IndividualTrait(NodeTrait):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.IndividualTrait
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:IndividualTrait"
    class_name: ClassVar[str] = "individual trait"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.IndividualTrait


@dataclass
class Triple(YAMLRoot):
    """
    Represents a single unadorned RDF triple
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Triple

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class Quad(Triple):
    """
    Represents an RDF triple plus named graph to which the triple belongs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.Quad
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:Quad"
    class_name: ClassVar[str] = "quad"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Quad

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None
    graph: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        if self.graph is not None and not isinstance(self.graph, NodeId):
            self.graph = NodeId(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class Statement(Quad):
    """
    A quad that is optionally adorned with statements about it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.Statement
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:Statement"
    class_name: ClassVar[str] = "statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Statement

    node_statements: Optional[Union[Union[dict, "NodeToNodeStatement"], List[Union[dict, "NodeToNodeStatement"]]]] = empty_list()
    value_statements: Optional[Union[Union[dict, "NodeToValueStatement"], List[Union[dict, "NodeToValueStatement"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.node_statements, list):
            self.node_statements = [self.node_statements] if self.node_statements is not None else []
        self.node_statements = [v if isinstance(v, NodeToNodeStatement) else NodeToNodeStatement(**as_dict(v)) for v in self.node_statements]

        if not isinstance(self.value_statements, list):
            self.value_statements = [self.value_statements] if self.value_statements is not None else []
        self.value_statements = [v if isinstance(v, NodeToValueStatement) else NodeToValueStatement(**as_dict(v)) for v in self.value_statements]

        super().__post_init__(**kwargs)


@dataclass
class NodeToNodeTriple(Triple):
    """
    A triple where object is a node (isIRI)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NodeToNodeTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NodeToNodeTriple"
    class_name: ClassVar[str] = "node to node triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeToNodeTriple

    object: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class NodeToNodeStatement(Statement):
    """
    A statement where object is a node (isIRI)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NodeToNodeStatement
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NodeToNodeStatement"
    class_name: ClassVar[str] = "node to node statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeToNodeStatement

    object: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        super().__post_init__(**kwargs)


class NamedNodeToNamedNodeTriple(NodeToNodeTriple):
    """
    A triple where subject and object are both nodes (isIRI)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NamedNodeToNamedNodeTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NamedNodeToNamedNodeTriple"
    class_name: ClassVar[str] = "named node to named node triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NamedNodeToNamedNodeTriple


@dataclass
class NodeToValueTriple(Triple):
    """
    A triple where object is a literal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NodeToValueTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NodeToValueTriple"
    class_name: ClassVar[str] = "node to value triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeToValueTriple

    object: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class NodeToValueStatement(Statement):
    """
    A statement where object is a literal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NodeToValueStatement
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NodeToValueStatement"
    class_name: ClassVar[str] = "node to value statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeToValueStatement

    object: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RdfTypeTriple(NodeToNodeTriple):
    """
    A triple that indicates the asserted type of the subject entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfTypeTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfTypeTriple"
    class_name: ClassVar[str] = "rdf type triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfTypeTriple

    object: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, ClassNodeId):
            self.object = ClassNodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RdfTypeStatement(NodeToNodeStatement):
    """
    A statement that indicates the asserted type of the subject entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfTypeStatement
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfTypeStatement"
    class_name: ClassVar[str] = "rdf type statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfTypeStatement

    object: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is not None and not isinstance(self.object, ClassNodeId):
            self.object = ClassNodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RdfsSubclassOfTriple(NodeToNodeTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsSubclassOfTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsSubclassOfTriple"
    class_name: ClassVar[str] = "rdfs subclass of triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsSubclassOfTriple

    subject: Optional[Union[str, ClassNodeId]] = None
    object: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, ClassNodeId):
            self.subject = ClassNodeId(self.subject)

        if self.object is not None and not isinstance(self.object, ClassNodeId):
            self.object = ClassNodeId(self.object)

        super().__post_init__(**kwargs)


class RdfsSubclassOfNamedTriple(RdfsSubclassOfTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsSubclassOfNamedTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsSubclassOfNamedTriple"
    class_name: ClassVar[str] = "rdfs subclass of named triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsSubclassOfNamedTriple


@dataclass
class RdfsSubpropertyOfTriple(NodeToNodeTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsSubpropertyOfTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsSubpropertyOfTriple"
    class_name: ClassVar[str] = "rdfs subproperty of triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsSubpropertyOfTriple

    subject: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[Union[str, PropertyNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, PropertyNodeId):
            self.subject = PropertyNodeId(self.subject)

        if self.object is not None and not isinstance(self.object, PropertyNodeId):
            self.object = PropertyNodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RdfsLabelTriple(NodeToValueTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsLabelTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsLabelTriple"
    class_name: ClassVar[str] = "rdfs label triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsLabelTriple

    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


class RdfsDomainTriple(NodeToNodeTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsDomainTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsDomainTriple"
    class_name: ClassVar[str] = "rdfs domain triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsDomainTriple


class RdfsRangeTriple(NodeToNodeTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RdfsRangeTriple
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RdfsRangeTriple"
    class_name: ClassVar[str] = "rdfs range triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RdfsRangeTriple


@dataclass
class Node(YAMLRoot):
    """
    The basic unit of representation in an RDF or OWL graph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.Node
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:Node"
    class_name: ClassVar[str] = "node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Node

    id: Union[str, NodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeId):
            self.id = NodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BlankNode(Node):
    """
    A node with an ID that is not preserved between databases
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.BlankNode
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:BlankNode"
    class_name: ClassVar[str] = "blank node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BlankNode

    id: Union[str, BlankNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BlankNodeId):
            self.id = BlankNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class IriNode(Node):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.IriNode
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:IriNode"
    class_name: ClassVar[str] = "iri node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.IriNode

    id: Union[str, IriNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IriNodeId):
            self.id = IriNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TypedNode(Node):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.TypedNode
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:TypedNode"
    class_name: ClassVar[str] = "typed node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TypedNode

    id: Union[str, TypedNodeId] = None
    type: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TypedNodeId):
            self.id = TypedNodeId(self.id)

        if self.type is not None and not isinstance(self.type, NodeId):
            self.type = NodeId(self.type)

        super().__post_init__(**kwargs)


@dataclass
class ClassNode(TypedNode):
    """
    A node that represents an RDFS/OWL class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "class node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ClassNode

    id: Union[str, ClassNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassNodeId):
            self.id = ClassNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PropertyNode(TypedNode):
    """
    Note this only directly classifies nodes asserted to be rdf:Properties
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Property
    class_class_curie: ClassVar[str] = "owl:Property"
    class_name: ClassVar[str] = "property node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PropertyNode

    id: Union[str, PropertyNodeId] = None

@dataclass
class NamedIndividualNode(Node):
    """
    A node that represents an OWL Named Individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.NamedIndividual
    class_class_curie: ClassVar[str] = "owl:NamedIndividual"
    class_name: ClassVar[str] = "named individual node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NamedIndividualNode

    id: Union[str, NamedIndividualNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedIndividualNodeId):
            self.id = NamedIndividualNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NestedTriple(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "nested triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NestedTriple

    xobject: Optional[Union[str, NodeId]] = None
    subject: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.xobject is not None and not isinstance(self.xobject, NodeId):
            self.xobject = NodeId(self.xobject)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class NodeObject(Node):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Resource
    class_class_curie: ClassVar[str] = "rdf:Resource"
    class_name: ClassVar[str] = "node object"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NodeObject

    id: Union[str, NodeObjectId] = None
    node_statements: Optional[Union[Union[dict, NodeToNodeStatement], List[Union[dict, NodeToNodeStatement]]]] = empty_list()
    value_statements: Optional[Union[Union[dict, NodeToValueStatement], List[Union[dict, NodeToValueStatement]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeObjectId):
            self.id = NodeObjectId(self.id)

        if not isinstance(self.node_statements, list):
            self.node_statements = [self.node_statements] if self.node_statements is not None else []
        self.node_statements = [v if isinstance(v, NodeToNodeStatement) else NodeToNodeStatement(**as_dict(v)) for v in self.node_statements]

        if not isinstance(self.value_statements, list):
            self.value_statements = [self.value_statements] if self.value_statements is not None else []
        self.value_statements = [v if isinstance(v, NodeToValueStatement) else NodeToValueStatement(**as_dict(v)) for v in self.value_statements]

        super().__post_init__(**kwargs)


@dataclass
class NestedNodeObject(Node):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Resource
    class_class_curie: ClassVar[str] = "rdf:Resource"
    class_name: ClassVar[str] = "nested node object"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NestedNodeObject

    id: Union[str, NestedNodeObjectId] = None
    node_statements: Optional[Union[Union[dict, NodeToNodeStatement], List[Union[dict, NodeToNodeStatement]]]] = empty_list()
    value_statements: Optional[Union[Union[dict, NodeToValueStatement], List[Union[dict, NodeToValueStatement]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NestedNodeObjectId):
            self.id = NestedNodeObjectId(self.id)

        if not isinstance(self.node_statements, list):
            self.node_statements = [self.node_statements] if self.node_statements is not None else []
        self.node_statements = [v if isinstance(v, NodeToNodeStatement) else NodeToNodeStatement(**as_dict(v)) for v in self.node_statements]

        if not isinstance(self.value_statements, list):
            self.value_statements = [self.value_statements] if self.value_statements is not None else []
        self.value_statements = [v if isinstance(v, NodeToValueStatement) else NodeToValueStatement(**as_dict(v)) for v in self.value_statements]

        super().__post_init__(**kwargs)


@dataclass
class BasicClass(Node):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "basic class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BasicClass

    id: Union[str, BasicClassId] = None
    subClassOf: Optional[Union[Union[str, ClassNodeId], List[Union[str, ClassNodeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BasicClassId):
            self.id = BasicClassId(self.id)

        if not isinstance(self.subClassOf, list):
            self.subClassOf = [self.subClassOf] if self.subClassOf is not None else []
        self.subClassOf = [v if isinstance(v, ClassNodeId) else ClassNodeId(v) for v in self.subClassOf]

        super().__post_init__(**kwargs)


@dataclass
class EquivalenceTripleMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.EquivalenceTripleMixin
    class_class_curie: ClassVar[str] = "sparqlfun_owl:EquivalenceTripleMixin"
    class_name: ClassVar[str] = "equivalence triple mixin"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.EquivalenceTripleMixin

    subject: Optional[Union[str, ClassNodeId]] = None
    object: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, ClassNodeId):
            self.subject = ClassNodeId(self.subject)

        if self.object is not None and not isinstance(self.object, ClassNodeId):
            self.object = ClassNodeId(self.object)

        super().__post_init__(**kwargs)


class OwlEquivalentClassTriple(NodeToNodeTriple):
    """
    A statement that connects two class nodes where both classes are equivalent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.OwlEquivalentClassTriple
    class_class_curie: ClassVar[str] = "sparqlfun_owl:OwlEquivalentClassTriple"
    class_name: ClassVar[str] = "owl equivalent class triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OwlEquivalentClassTriple


@dataclass
class OwlNamedEquivalentClassTriple(NamedNodeToNamedNodeTriple):
    """
    An equivalence triple between two named classes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.OwlNamedEquivalentClassTriple
    class_class_curie: ClassVar[str] = "sparqlfun_owl:OwlNamedEquivalentClassTriple"
    class_name: ClassVar[str] = "owl named equivalent class triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OwlNamedEquivalentClassTriple

    subject: Optional[Union[str, ClassNodeId]] = None
    object: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, ClassNodeId):
            self.subject = ClassNodeId(self.subject)

        if self.object is not None and not isinstance(self.object, ClassNodeId):
            self.object = ClassNodeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SomeValuesFromRestriction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Restriction
    class_class_curie: ClassVar[str] = "owl:Restriction"
    class_name: ClassVar[str] = "some values from restriction"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SomeValuesFromRestriction

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, PropertyNodeId]] = None
    filler: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        if self.filler is not None and not isinstance(self.filler, NodeId):
            self.filler = NodeId(self.filler)

        super().__post_init__(**kwargs)


class SubclassOfSomeValuesFrom(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.SubclassOfSomeValuesFrom
    class_class_curie: ClassVar[str] = "sparqlfun_owl:SubclassOfSomeValuesFrom"
    class_name: ClassVar[str] = "subclass of some values from"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubclassOfSomeValuesFrom


@dataclass
class DescribeEquivalentExpression(ResultSet):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.DescribeEquivalentExpression
    class_class_curie: ClassVar[str] = "sparqlfun_owl:DescribeEquivalentExpression"
    class_name: ClassVar[str] = "describe equivalent expression"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DescribeEquivalentExpression

    results: Optional[Union[Union[str, ClassNodeId], List[Union[str, ClassNodeId]]]] = empty_list()
    subject: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, ClassNodeId) else ClassNodeId(v) for v in self.results]

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OwlTripleAnnotation(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.OwlTripleAnnotation
    class_class_curie: ClassVar[str] = "sparqlfun_owl:OwlTripleAnnotation"
    class_name: ClassVar[str] = "owl triple annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OwlTripleAnnotation

    axiom_identifier: Optional[Union[str, BlankNodeId]] = None
    axiom_predicate: Optional[Union[str, PropertyNodeId]] = None
    axiom_object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.axiom_identifier is not None and not isinstance(self.axiom_identifier, BlankNodeId):
            self.axiom_identifier = BlankNodeId(self.axiom_identifier)

        if self.axiom_predicate is not None and not isinstance(self.axiom_predicate, PropertyNodeId):
            self.axiom_predicate = PropertyNodeId(self.axiom_predicate)

        super().__post_init__(**kwargs)


@dataclass
class OwlTripleWithAnnotationsTODO(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.OwlTripleWithAnnotationsTODO
    class_class_curie: ClassVar[str] = "sparqlfun_owl:OwlTripleWithAnnotationsTODO"
    class_name: ClassVar[str] = "owl triple with annotations TODO"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OwlTripleWithAnnotationsTODO

    annotations: Optional[Union[dict, "OwlAnnotation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.annotations is not None and not isinstance(self.annotations, OwlAnnotation):
            self.annotations = OwlAnnotation(**as_dict(self.annotations))

        super().__post_init__(**kwargs)


@dataclass
class OwlAnnotation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.OwlAnnotation
    class_class_curie: ClassVar[str] = "sparqlfun_owl:OwlAnnotation"
    class_name: ClassVar[str] = "owl annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OwlAnnotation

    predicate: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class TraversalBasedPairwiseDisjointnessViolation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OWL.TraversalBasedPairwiseDisjointnessViolation
    class_class_curie: ClassVar[str] = "sparqlfun_owl:TraversalBasedPairwiseDisjointnessViolation"
    class_name: ClassVar[str] = "traversal based pairwise disjointness violation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TraversalBasedPairwiseDisjointnessViolation

    class1: Optional[Union[str, NodeId]] = None
    class2: Optional[Union[str, NodeId]] = None
    descendant_class: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.class1 is not None and not isinstance(self.class1, NodeId):
            self.class1 = NodeId(self.class1)

        if self.class2 is not None and not isinstance(self.class2, NodeId):
            self.class2 = NodeId(self.class2)

        if self.descendant_class is not None and not isinstance(self.descendant_class, NodeId):
            self.descendant_class = NodeId(self.descendant_class)

        super().__post_init__(**kwargs)


@dataclass
class RelationGraphQuad(Quad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.RelationGraphQuad
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:RelationGraphQuad"
    class_name: ClassVar[str] = "relation graph quad"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RelationGraphQuad

    graph: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.graph is not None and not isinstance(self.graph, NodeId):
            self.graph = NodeId(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class NonRedundantQuad(RelationGraphQuad):
    """
    A triple that indicates the asserted type of the subject entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.NonRedundantQuad
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:NonRedundantQuad"
    class_name: ClassVar[str] = "non redundant quad"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NonRedundantQuad

    graph: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.graph is not None and not isinstance(self.graph, ClassNodeId):
            self.graph = ClassNodeId(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class TaxonApplicableClass(ClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.TaxonApplicableClass
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:TaxonApplicableClass"
    class_name: ClassVar[str] = "taxon applicable class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TaxonApplicableClass

    id: Union[str, TaxonApplicableClassId] = None

@dataclass
class TaxonClass(ClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.TaxonClass
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:TaxonClass"
    class_name: ClassVar[str] = "taxon class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TaxonClass

    id: Union[str, TaxonClassId] = None

@dataclass
class TaxonApplicable(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.TaxonApplicable
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:TaxonApplicable"
    class_name: ClassVar[str] = "taxon applicable"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TaxonApplicable

    subject: Optional[Union[str, TaxonApplicableClassId]] = None
    object: Optional[Union[str, TaxonClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, TaxonApplicableClassId):
            self.subject = TaxonApplicableClassId(self.subject)

        if self.object is not None and not isinstance(self.object, TaxonClassId):
            self.object = TaxonClassId(self.object)

        super().__post_init__(**kwargs)


class NeverInTaxonTriple(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.NeverInTaxonTriple
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:NeverInTaxonTriple"
    class_name: ClassVar[str] = "never in taxon triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NeverInTaxonTriple


class InTaxonTriple(Triple):
    """
    In ubergraph, an in-taxon triple is pre-inferred
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.InTaxonTriple
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:InTaxonTriple"
    class_name: ClassVar[str] = "in taxon triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.InTaxonTriple


class DefinitionTriple(NodeToValueTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.DefinitionTriple
    class_class_curie: ClassVar[str] = "sparqlfun_omo:DefinitionTriple"
    class_name: ClassVar[str] = "definition triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DefinitionTriple


class ConformsToTriple(NodeToNodeTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.ConformsToTriple
    class_class_curie: ClassVar[str] = "sparqlfun_omo:ConformsToTriple"
    class_name: ClassVar[str] = "conforms to triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ConformsToTriple


class ConformsToStatement(NodeToNodeStatement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.ConformsToStatement
    class_class_curie: ClassVar[str] = "sparqlfun_omo:ConformsToStatement"
    class_name: ClassVar[str] = "conforms to statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ConformsToStatement


@dataclass
class GraphClassNode(ClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.GraphClassNode
    class_class_curie: ClassVar[str] = "sparqlfun_omo:GraphClassNode"
    class_name: ClassVar[str] = "graph class node"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GraphClassNode

    id: Union[str, GraphClassNodeId] = None
    graph: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GraphClassNodeId):
            self.id = GraphClassNodeId(self.id)

        if self.graph is not None and not isinstance(self.graph, NodeId):
            self.graph = NodeId(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class OboClass(GraphClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "obo class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OboClass

    id: Union[str, OboClassId] = None
    label: Optional[str] = None
    definition: Optional[str] = None
    exact_synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OboClassId):
            self.id = OboClassId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        super().__post_init__(**kwargs)


@dataclass
class OboClassQuery(ResultSet):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.OboClassQuery
    class_class_curie: ClassVar[str] = "sparqlfun_omo:OboClassQuery"
    class_name: ClassVar[str] = "obo class query"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OboClassQuery

    results: Optional[Union[Union[str, OboClassId], List[Union[str, OboClassId]]]] = empty_list()
    label_regex: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, OboClassId) else OboClassId(v) for v in self.results]

        if self.label_regex is not None and not isinstance(self.label_regex, str):
            self.label_regex = str(self.label_regex)

        super().__post_init__(**kwargs)


@dataclass
class DeprecatedOboClassQuery(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN.OboClassQuery
    class_class_curie: ClassVar[str] = "sparqlfun:OboClassQuery"
    class_name: ClassVar[str] = "deprecated obo class query"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DeprecatedOboClassQuery

    results: Optional[Union[Union[str, OboClassId], List[Union[str, OboClassId]]]] = empty_list()
    label_regex: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, OboClassId) else OboClassId(v) for v in self.results]

        if self.label_regex is not None and not isinstance(self.label_regex, str):
            self.label_regex = str(self.label_regex)

        super().__post_init__(**kwargs)


@dataclass
class UbergraphTaxonClass(TaxonClass):
    """
    all classes representing a taxon in ubergraph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.UbergraphTaxonClass
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:UbergraphTaxonClass"
    class_name: ClassVar[str] = "ubergraph taxon class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UbergraphTaxonClass

    id: Union[str, UbergraphTaxonClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UbergraphTaxonClassId):
            self.id = UbergraphTaxonClassId(self.id)

        super().__post_init__(**kwargs)


class UbergraphQuad(RelationGraphQuad):
    """
    a quad in an ubergraph endpoint
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.UbergraphQuad
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:UbergraphQuad"
    class_name: ClassVar[str] = "ubergraph quad"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UbergraphQuad


class NormalizedInformationContentTriple(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.NormalizedInformationContentTriple
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:NormalizedInformationContentTriple"
    class_name: ClassVar[str] = "normalized information content triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NormalizedInformationContentTriple


class SubClassCountTriple(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.SubClassCountTriple
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:SubClassCountTriple"
    class_name: ClassVar[str] = "SubClass count triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubClassCountTriple


class IsAOrPartOf(UbergraphQuad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.IsAOrPartOf
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:IsAOrPartOf"
    class_name: ClassVar[str] = "is a or part of"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.IsAOrPartOf


@dataclass
class ClassTaxonExclusionViaNeverIn(Triple):
    """
    An inferred never-in between a subject term and an object taxon, which holds
    when the inferred direct taxon is not in an ancestry relationship with the object taxon
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.ClassTaxonExclusionViaNeverIn
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:ClassTaxonExclusionViaNeverIn"
    class_name: ClassVar[str] = "class taxon exclusion via never in"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ClassTaxonExclusionViaNeverIn

    subject_predicate: Optional[Union[str, NodeId]] = None
    class_with_constraint: Optional[Union[str, NodeId]] = None
    direct_taxon: Optional[Union[str, NodeId]] = None
    subject: Optional[Union[str, NodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_predicate is not None and not isinstance(self.subject_predicate, NodeId):
            self.subject_predicate = NodeId(self.subject_predicate)

        if self.class_with_constraint is not None and not isinstance(self.class_with_constraint, NodeId):
            self.class_with_constraint = NodeId(self.class_with_constraint)

        if self.direct_taxon is not None and not isinstance(self.direct_taxon, NodeId):
            self.direct_taxon = NodeId(self.direct_taxon)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ClassTaxonExclusionViaOnlyIn(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.ClassTaxonExclusionViaOnlyIn
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:ClassTaxonExclusionViaOnlyIn"
    class_name: ClassVar[str] = "class taxon exclusion via only in"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ClassTaxonExclusionViaOnlyIn

    subject_predicate: Optional[Union[str, NodeId]] = None
    class_with_constraint: Optional[Union[str, NodeId]] = None
    direct_taxon: Optional[Union[str, NodeId]] = None
    subject: Optional[Union[str, NodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_predicate is not None and not isinstance(self.subject_predicate, NodeId):
            self.subject_predicate = NodeId(self.subject_predicate)

        if self.class_with_constraint is not None and not isinstance(self.class_with_constraint, NodeId):
            self.class_with_constraint = NodeId(self.class_with_constraint)

        if self.direct_taxon is not None and not isinstance(self.direct_taxon, NodeId):
            self.direct_taxon = NodeId(self.direct_taxon)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ClassTaxonExclusion(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.ClassTaxonExclusion
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:ClassTaxonExclusion"
    class_name: ClassVar[str] = "class taxon exclusion"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ClassTaxonExclusion

    subject_predicate: Optional[Union[str, NodeId]] = None
    class_with_constraint: Optional[Union[str, NodeId]] = None
    direct_taxon: Optional[Union[str, NodeId]] = None
    subject: Optional[Union[str, NodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_predicate is not None and not isinstance(self.subject_predicate, NodeId):
            self.subject_predicate = NodeId(self.subject_predicate)

        if self.class_with_constraint is not None and not isinstance(self.class_with_constraint, NodeId):
            self.class_with_constraint = NodeId(self.class_with_constraint)

        if self.direct_taxon is not None and not isinstance(self.direct_taxon, NodeId):
            self.direct_taxon = NodeId(self.direct_taxon)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class SetwiseCommonSubClassAncestor(YAMLRoot):
    """
    Common superclass ancestor to a set of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.SetwiseCommonSubClassAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:SetwiseCommonSubClassAncestor"
    class_name: ClassVar[str] = "setwise common SubClass ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SetwiseCommonSubClassAncestor

    nodes: Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]] = empty_list()
    ancestor: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeId) else NodeId(v) for v in self.nodes]

        if self.ancestor is not None and not isinstance(self.ancestor, NodeId):
            self.ancestor = NodeId(self.ancestor)

        super().__post_init__(**kwargs)


@dataclass
class SetwiseMostRecentCommonSubClassAncestor(YAMLRoot):
    """
    Most recent common superclass ancestor to a set of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.SetwiseMostRecentCommonSubClassAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:SetwiseMostRecentCommonSubClassAncestor"
    class_name: ClassVar[str] = "setwise most recent common SubClass ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SetwiseMostRecentCommonSubClassAncestor

    nodes: Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]] = empty_list()
    ancestor: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeId) else NodeId(v) for v in self.nodes]

        if self.ancestor is not None and not isinstance(self.ancestor, NodeId):
            self.ancestor = NodeId(self.ancestor)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseCommonAncestor(YAMLRoot):
    """
    Common ancestor in relation graph over any relations between two nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonAncestor"
    class_name: ClassVar[str] = "pairwise common ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonAncestor

    node1: Optional[Union[str, NodeId]] = None
    node2: Optional[Union[str, NodeId]] = None
    predicate1: Optional[Union[str, PropertyNodeId]] = None
    predicate2: Optional[Union[str, PropertyNodeId]] = None
    ancestor: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, NodeId):
            self.node1 = NodeId(self.node1)

        if self.node2 is not None and not isinstance(self.node2, NodeId):
            self.node2 = NodeId(self.node2)

        if self.predicate1 is not None and not isinstance(self.predicate1, PropertyNodeId):
            self.predicate1 = PropertyNodeId(self.predicate1)

        if self.predicate2 is not None and not isinstance(self.predicate2, PropertyNodeId):
            self.predicate2 = PropertyNodeId(self.predicate2)

        if self.ancestor is not None and not isinstance(self.ancestor, NodeId):
            self.ancestor = NodeId(self.ancestor)

        super().__post_init__(**kwargs)


class PairwiseCommonSubClassAncestor(PairwiseCommonAncestor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonSubClassAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonSubClassAncestor"
    class_name: ClassVar[str] = "pairwise common SubClass ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonSubClassAncestor


@dataclass
class PairwiseMostRecentCommonAncestor(YAMLRoot):
    """
    Common non-redundant ancestor in relation graph over any relations between two nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseMostRecentCommonAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseMostRecentCommonAncestor"
    class_name: ClassVar[str] = "pairwise most recent common ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseMostRecentCommonAncestor

    node1: Optional[Union[str, NodeId]] = None
    node2: Optional[Union[str, NodeId]] = None
    predicate1: Optional[Union[str, PropertyNodeId]] = None
    predicate2: Optional[Union[str, PropertyNodeId]] = None
    ancestor: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, NodeId):
            self.node1 = NodeId(self.node1)

        if self.node2 is not None and not isinstance(self.node2, NodeId):
            self.node2 = NodeId(self.node2)

        if self.predicate1 is not None and not isinstance(self.predicate1, PropertyNodeId):
            self.predicate1 = PropertyNodeId(self.predicate1)

        if self.predicate2 is not None and not isinstance(self.predicate2, PropertyNodeId):
            self.predicate2 = PropertyNodeId(self.predicate2)

        if self.ancestor is not None and not isinstance(self.ancestor, NodeId):
            self.ancestor = NodeId(self.ancestor)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseMostRecentCommonSubClassAncestor(YAMLRoot):
    """
    Common non-redundant SubClass ancestor between two nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseMostRecentCommonSubClassAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseMostRecentCommonSubClassAncestor"
    class_name: ClassVar[str] = "pairwise most recent common SubClass ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseMostRecentCommonSubClassAncestor

    node1: Optional[Union[str, NodeId]] = None
    node2: Optional[Union[str, NodeId]] = None
    ancestor: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, NodeId):
            self.node1 = NodeId(self.node1)

        if self.node2 is not None and not isinstance(self.node2, NodeId):
            self.node2 = NodeId(self.node2)

        if self.ancestor is not None and not isinstance(self.ancestor, NodeId):
            self.ancestor = NodeId(self.ancestor)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseCommonDescendant(YAMLRoot):
    """
    Common descendant in relation graph over any relations between two nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonDescendant
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonDescendant"
    class_name: ClassVar[str] = "pairwise common descendant"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonDescendant

    node1: Optional[Union[str, NodeId]] = None
    node2: Optional[Union[str, NodeId]] = None
    predicate1: Optional[Union[str, PropertyNodeId]] = None
    predicate2: Optional[Union[str, PropertyNodeId]] = None
    descendant: Optional[Union[str, NodeId]] = None
    is_direction_canonical: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, NodeId):
            self.node1 = NodeId(self.node1)

        if self.node2 is not None and not isinstance(self.node2, NodeId):
            self.node2 = NodeId(self.node2)

        if self.predicate1 is not None and not isinstance(self.predicate1, PropertyNodeId):
            self.predicate1 = PropertyNodeId(self.predicate1)

        if self.predicate2 is not None and not isinstance(self.predicate2, PropertyNodeId):
            self.predicate2 = PropertyNodeId(self.predicate2)

        if self.descendant is not None and not isinstance(self.descendant, NodeId):
            self.descendant = NodeId(self.descendant)

        if self.is_direction_canonical is not None and not isinstance(self.is_direction_canonical, Bool):
            self.is_direction_canonical = Bool(self.is_direction_canonical)

        super().__post_init__(**kwargs)


class PairwiseCommonSubClassDescendant(PairwiseCommonDescendant):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonSubClassDescendant
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonSubClassDescendant"
    class_name: ClassVar[str] = "pairwise common SubClass descendant"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonSubClassDescendant


@dataclass
class PairwiseCommonDescendantMatrix(YAMLRoot):
    """
    Common descendant in relation graph over any relations between two nodes from two axes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonDescendantMatrix
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonDescendantMatrix"
    class_name: ClassVar[str] = "pairwise common descendant matrix"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonDescendantMatrix

    node1: Optional[Union[str, NodeId]] = None
    node2: Optional[Union[str, NodeId]] = None
    node1_candidates: Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]] = empty_list()
    node2_candidates: Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]] = empty_list()
    predicate1: Optional[Union[str, PropertyNodeId]] = None
    predicate2: Optional[Union[str, PropertyNodeId]] = None
    descendant: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, NodeId):
            self.node1 = NodeId(self.node1)

        if self.node2 is not None and not isinstance(self.node2, NodeId):
            self.node2 = NodeId(self.node2)

        if not isinstance(self.node1_candidates, list):
            self.node1_candidates = [self.node1_candidates] if self.node1_candidates is not None else []
        self.node1_candidates = [v if isinstance(v, NodeId) else NodeId(v) for v in self.node1_candidates]

        if not isinstance(self.node2_candidates, list):
            self.node2_candidates = [self.node2_candidates] if self.node2_candidates is not None else []
        self.node2_candidates = [v if isinstance(v, NodeId) else NodeId(v) for v in self.node2_candidates]

        if self.predicate1 is not None and not isinstance(self.predicate1, PropertyNodeId):
            self.predicate1 = PropertyNodeId(self.predicate1)

        if self.predicate2 is not None and not isinstance(self.predicate2, PropertyNodeId):
            self.predicate2 = PropertyNodeId(self.predicate2)

        if self.descendant is not None and not isinstance(self.descendant, NodeId):
            self.descendant = NodeId(self.descendant)

        super().__post_init__(**kwargs)


class PairwiseCommonSubClassDescendantMatrix(PairwiseCommonDescendantMatrix):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonSubClassDescendantMatrix
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonSubClassDescendantMatrix"
    class_name: ClassVar[str] = "pairwise common SubClass descendant matrix"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonSubClassDescendantMatrix


@dataclass
class OboClassFiltered(ClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "obo class filtered"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OboClassFiltered

    id: Union[str, OboClassFilteredId] = None
    definition: Optional[str] = None
    exact_synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OboClassFilteredId):
            self.id = OboClassFilteredId(self.id)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        super().__post_init__(**kwargs)


@dataclass
class ProteinClassifiedWith(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.ProteinClassifiedWith
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:ProteinClassifiedWith"
    class_name: ClassVar[str] = "protein classified with"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ProteinClassifiedWith

    subject: Optional[Union[str, NodeId]] = None
    object: Optional[Union[dict, NodeOrLiteral]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OboClassWithCategory(OboClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0001062"]
    class_class_curie: ClassVar[str] = "UBERON:0001062"
    class_name: ClassVar[str] = "obo class with category"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OboClassWithCategory

    id: Union[str, OboClassWithCategoryId] = None
    category: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OboClassWithCategoryId):
            self.id = OboClassWithCategoryId(self.id)

        if self.category is not None and not isinstance(self.category, ClassNodeId):
            self.category = ClassNodeId(self.category)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(OboClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0001062"]
    class_class_curie: ClassVar[str] = "UBERON:0001062"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BloodVessel(OboClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0001981"]
    class_class_curie: ClassVar[str] = "UBERON:0001981"
    class_name: ClassVar[str] = "blood vessel"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BloodVessel

    id: Union[str, BloodVesselId] = None
    subcategory: Optional[Union[str, "BloodVesselSubcategory"]] = None
    supplies: Optional[Union[str, AnatomicalEntityId]] = None
    drains: Optional[Union[str, AnatomicalEntityId]] = None
    branching_part_of: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BloodVesselId):
            self.id = BloodVesselId(self.id)

        if self.subcategory is not None and not isinstance(self.subcategory, BloodVesselSubcategory):
            self.subcategory = BloodVesselSubcategory(self.subcategory)

        if self.supplies is not None and not isinstance(self.supplies, AnatomicalEntityId):
            self.supplies = AnatomicalEntityId(self.supplies)

        if self.drains is not None and not isinstance(self.drains, AnatomicalEntityId):
            self.drains = AnatomicalEntityId(self.drains)

        if self.branching_part_of is not None and not isinstance(self.branching_part_of, AnatomicalEntityId):
            self.branching_part_of = AnatomicalEntityId(self.branching_part_of)

        super().__post_init__(**kwargs)


@dataclass
class CellType(OboClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "cell type"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CellType

    id: Union[str, CellTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        super().__post_init__(**kwargs)


class BiolinkCategoryTriple(NodeToNodeTriple):
    """
    A triple that connects any node to its biolink category
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_BIOLINK.BiolinkCategoryTriple
    class_class_curie: ClassVar[str] = "sparqlfun_biolink:BiolinkCategoryTriple"
    class_name: ClassVar[str] = "biolink category triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BiolinkCategoryTriple


@dataclass
class Association(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_BIOLINK.Association
    class_class_curie: ClassVar[str] = "sparqlfun_biolink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Association

    subject_category: Optional[Union[str, ClassNodeId]] = None
    object_category: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_category is not None and not isinstance(self.subject_category, ClassNodeId):
            self.subject_category = ClassNodeId(self.subject_category)

        if self.object_category is not None and not isinstance(self.object_category, ClassNodeId):
            self.object_category = ClassNodeId(self.object_category)

        super().__post_init__(**kwargs)


@dataclass
class AssociationWithInferredCategories(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_BIOLINK.AssociationWithInferredCategories
    class_class_curie: ClassVar[str] = "sparqlfun_biolink:AssociationWithInferredCategories"
    class_name: ClassVar[str] = "association with inferred categories"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AssociationWithInferredCategories

    subject_category: Optional[Union[str, ClassNodeId]] = None
    object_category: Optional[Union[str, ClassNodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_category is not None and not isinstance(self.subject_category, ClassNodeId):
            self.subject_category = ClassNodeId(self.subject_category)

        if self.object_category is not None and not isinstance(self.object_category, ClassNodeId):
            self.object_category = ClassNodeId(self.object_category)

        super().__post_init__(**kwargs)


class GeneToGeneAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_BIOLINK.GeneToGeneAssociation
    class_class_curie: ClassVar[str] = "sparqlfun_biolink:GeneToGeneAssociation"
    class_name: ClassVar[str] = "gene to gene association"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GeneToGeneAssociation


@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Thing
    class_class_curie: ClassVar[str] = "upcore:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Thing

    id: Union[str, ThingId] = None
    type: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if self.type is not None and not isinstance(self.type, NodeId):
            self.type = NodeId(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Protein(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Protein
    class_class_curie: ClassVar[str] = "upcore:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Protein

    id: Union[str, ProteinId] = None
    mappedCitation: Optional[Union[str, CitationId]] = None
    seeAlso: Optional[Union[str, ThingId]] = None
    annotation: Optional[Union[dict, "Annotation"]] = None
    mappedAnnotation: Optional[Union[dict, "Annotation"]] = None
    classifiedWith: Optional[Union[str, ConceptId]] = None
    citation: Optional[Union[str, CitationId]] = None
    oldMnemonic: Optional[str] = None
    isolatedFrom: Optional[Union[dict, "Tissue"]] = None
    attribution: Optional[Union[dict, "Attribution"]] = None
    organism: Optional[Union[str, TaxonId]] = None
    encodedBy: Optional[Union[str, GeneId]] = None
    mnemonic: Optional[str] = None
    interaction: Optional[Union[dict, "Interaction"]] = None
    representativeFor: Optional[Union[str, ClusterId]] = None
    created: Optional[Union[str, XSDDate]] = None
    conflictingSequence: Optional[Union[dict, "ExternalSequence"]] = None
    potentialSequence: Optional[Union[dict, "Sequence"]] = None
    version: Optional[int] = None
    type: Optional[Union[str, NodeId]] = None
    seedFor: Optional[Union[str, ClusterId]] = None
    sequence: Optional[Union[dict, "Sequence"]] = None
    alternativeName: Optional[Union[dict, "StructuredName"]] = None
    reviewed: Optional[Union[bool, Bool]] = None
    recommendedName: Optional[Union[dict, "StructuredName"]] = None
    submittedName: Optional[Union[dict, "StructuredName"]] = None
    modified: Optional[Union[str, XSDDate]] = None
    enzyme: Optional[Union[str, EnzymeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.mappedCitation is not None and not isinstance(self.mappedCitation, CitationId):
            self.mappedCitation = CitationId(self.mappedCitation)

        if self.seeAlso is not None and not isinstance(self.seeAlso, ThingId):
            self.seeAlso = ThingId(self.seeAlso)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation()

        if self.mappedAnnotation is not None and not isinstance(self.mappedAnnotation, Annotation):
            self.mappedAnnotation = Annotation()

        if self.classifiedWith is not None and not isinstance(self.classifiedWith, ConceptId):
            self.classifiedWith = ConceptId(self.classifiedWith)

        if self.citation is not None and not isinstance(self.citation, CitationId):
            self.citation = CitationId(self.citation)

        if self.oldMnemonic is not None and not isinstance(self.oldMnemonic, str):
            self.oldMnemonic = str(self.oldMnemonic)

        if self.isolatedFrom is not None and not isinstance(self.isolatedFrom, Tissue):
            self.isolatedFrom = Tissue()

        if self.attribution is not None and not isinstance(self.attribution, Attribution):
            self.attribution = Attribution()

        if self.organism is not None and not isinstance(self.organism, TaxonId):
            self.organism = TaxonId(self.organism)

        if self.encodedBy is not None and not isinstance(self.encodedBy, GeneId):
            self.encodedBy = GeneId(self.encodedBy)

        if self.mnemonic is not None and not isinstance(self.mnemonic, str):
            self.mnemonic = str(self.mnemonic)

        if self.interaction is not None and not isinstance(self.interaction, Interaction):
            self.interaction = Interaction()

        if self.representativeFor is not None and not isinstance(self.representativeFor, ClusterId):
            self.representativeFor = ClusterId(self.representativeFor)

        if self.created is not None and not isinstance(self.created, XSDDate):
            self.created = XSDDate(self.created)

        if self.conflictingSequence is not None and not isinstance(self.conflictingSequence, ExternalSequence):
            self.conflictingSequence = ExternalSequence()

        if self.potentialSequence is not None and not isinstance(self.potentialSequence, Sequence):
            self.potentialSequence = Sequence()

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if self.type is not None and not isinstance(self.type, NodeId):
            self.type = NodeId(self.type)

        if self.seedFor is not None and not isinstance(self.seedFor, ClusterId):
            self.seedFor = ClusterId(self.seedFor)

        if self.sequence is not None and not isinstance(self.sequence, Sequence):
            self.sequence = Sequence()

        if self.alternativeName is not None and not isinstance(self.alternativeName, StructuredName):
            self.alternativeName = StructuredName()

        if self.reviewed is not None and not isinstance(self.reviewed, Bool):
            self.reviewed = Bool(self.reviewed)

        if self.recommendedName is not None and not isinstance(self.recommendedName, StructuredName):
            self.recommendedName = StructuredName()

        if self.submittedName is not None and not isinstance(self.submittedName, StructuredName):
            self.submittedName = StructuredName()

        if self.modified is not None and not isinstance(self.modified, XSDDate):
            self.modified = XSDDate(self.modified)

        if self.enzyme is not None and not isinstance(self.enzyme, EnzymeId):
            self.enzyme = EnzymeId(self.enzyme)

        super().__post_init__(**kwargs)


@dataclass
class SubcellularLocation(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subcellular_Location
    class_class_curie: ClassVar[str] = "upcore:Subcellular_Location"
    class_name: ClassVar[str] = "Subcellular_Location"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubcellularLocation

    id: Union[str, SubcellularLocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubcellularLocationId):
            self.id = SubcellularLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Disease(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disease
    class_class_curie: ClassVar[str] = "upcore:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProteinExistence(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Protein_Existence
    class_class_curie: ClassVar[str] = "upcore:Protein_Existence"
    class_name: ClassVar[str] = "Protein_Existence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ProteinExistence

    id: Union[str, ProteinExistenceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinExistenceId):
            self.id = ProteinExistenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organelle(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Organelle
    class_class_curie: ClassVar[str] = "upcore:Organelle"
    class_name: ClassVar[str] = "Organelle"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Organelle

    id: Union[str, OrganelleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganelleId):
            self.id = OrganelleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FamilyMembershipStatement(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Family_Membership_Statement
    class_class_curie: ClassVar[str] = "upcore:Family_Membership_Statement"
    class_name: ClassVar[str] = "Family_Membership_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.FamilyMembershipStatement

    id: Union[str, FamilyMembershipStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyMembershipStatementId):
            self.id = FamilyMembershipStatementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Class(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Class

    id: Union[str, ClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassId):
            self.id = ClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Statement(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Statement

    id: Union[str, StatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatementId):
            self.id = StatementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Enzyme(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Enzyme
    class_class_curie: ClassVar[str] = "upcore:Enzyme"
    class_name: ClassVar[str] = "Enzyme"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Enzyme

    id: Union[str, EnzymeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnzymeId):
            self.id = EnzymeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Taxon(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Taxon
    class_class_curie: ClassVar[str] = "upcore:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Taxon

    id: Union[str, TaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonId):
            self.id = TaxonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Citation(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Citation
    class_class_curie: ClassVar[str] = "upcore:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Citation

    id: Union[str, CitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitationId):
            self.id = CitationId(self.id)

        super().__post_init__(**kwargs)


class CatalyticActivity(YAMLRoot):
    """
    The catalytic activity of an enzyme.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Catalytic_Activity
    class_class_curie: ClassVar[str] = "upcore:Catalytic_Activity"
    class_name: ClassVar[str] = "Catalytic_Activity"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CatalyticActivity


class Molecule(YAMLRoot):
    """
    A biological molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Molecule
    class_class_curie: ClassVar[str] = "upcore:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Molecule


class Tissue(YAMLRoot):
    """
    A tissue such as lung or heart.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Tissue
    class_class_curie: ClassVar[str] = "upcore:Tissue"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Tissue


class Sequence(YAMLRoot):
    """
    An amino acid sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence
    class_class_curie: ClassVar[str] = "upcore:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Sequence


class Participant(YAMLRoot):
    """
    A participant in a protein-protein interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Participant
    class_class_curie: ClassVar[str] = "upcore:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Participant


class NotObsolete(YAMLRoot):
    """
    A class introduced to group all records that are currently in the database.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete"
    class_name: ClassVar[str] = "Not_Obsolete"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NotObsolete


class StructuredName(YAMLRoot):
    """
    A resource that holds a set of the known names for this protein together.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structured_Name
    class_class_curie: ClassVar[str] = "upcore:Structured_Name"
    class_name: ClassVar[str] = "Structured_Name"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.StructuredName


class Status(YAMLRoot):
    """
    Indicator for the reliability of a piece of information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Status
    class_class_curie: ClassVar[str] = "upcore:Status"
    class_name: ClassVar[str] = "Status"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Status


class Method(YAMLRoot):
    """
    An experimental method.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Method
    class_class_curie: ClassVar[str] = "upcore:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Method


class Plasmid(YAMLRoot):
    """
    Description of a Plasmid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Plasmid
    class_class_curie: ClassVar[str] = "upcore:Plasmid"
    class_name: ClassVar[str] = "Plasmid"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Plasmid


class Resource(YAMLRoot):
    """
    A life science resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Resource
    class_class_curie: ClassVar[str] = "upcore:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Resource


class Annotation(YAMLRoot):
    """
    Description of a resource on a specific topic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Annotation
    class_class_curie: ClassVar[str] = "upcore:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Annotation


class Reviewed(YAMLRoot):
    """
    The class of all reviewed records in the database (i.e. records that where looked at by a curator for integration
    into the database).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reviewed
    class_class_curie: ClassVar[str] = "upcore:Reviewed"
    class_name: ClassVar[str] = "Reviewed"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Reviewed


class Interaction(YAMLRoot):
    """
    Description of a protein-protein interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Interaction
    class_class_curie: ClassVar[str] = "upcore:Interaction"
    class_name: ClassVar[str] = "Interaction"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Interaction


class Transposon(YAMLRoot):
    """
    A transposon
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transposon
    class_class_curie: ClassVar[str] = "upcore:Transposon"
    class_name: ClassVar[str] = "Transposon"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Transposon


class Pathway(YAMLRoot):
    """
    A hierarchical discription of a metabolic pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pathway
    class_class_curie: ClassVar[str] = "upcore:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Pathway


class Attribution(YAMLRoot):
    """
    Entity used to attach evidence or provenance to a rdf statement via reification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Attribution
    class_class_curie: ClassVar[str] = "upcore:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Attribution


class Strain(YAMLRoot):
    """
    A strain of a species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Strain
    class_class_curie: ClassVar[str] = "upcore:Strain"
    class_name: ClassVar[str] = "Strain"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Strain


class Rank(YAMLRoot):
    """
    A rank of a taxon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Rank
    class_class_curie: ClassVar[str] = "upcore:Rank"
    class_name: ClassVar[str] = "Rank"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Rank


class Obsolete(YAMLRoot):
    """
    The class of all obsolete records in the database (i.e. records that where once published but are now removed).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete
    class_class_curie: ClassVar[str] = "upcore:Obsolete"
    class_name: ClassVar[str] = "Obsolete"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Obsolete


class EnzymeRegulationAnnotation(YAMLRoot):
    """
    The use of this class has been replaced by Activity_Regulation_Annotation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Enzyme_Regulation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Enzyme_Regulation_Annotation"
    class_name: ClassVar[str] = "Enzyme_Regulation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.EnzymeRegulationAnnotation


class Proteome(YAMLRoot):
    """
    Description of a proteome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Proteome
    class_class_curie: ClassVar[str] = "upcore:Proteome"
    class_name: ClassVar[str] = "Proteome"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Proteome


@dataclass
class DomainAssignmentStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Assignment_Statement
    class_class_curie: ClassVar[str] = "upcore:Domain_Assignment_Statement"
    class_name: ClassVar[str] = "Domain_Assignment_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DomainAssignmentStatement

    id: Union[str, DomainAssignmentStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainAssignmentStatementId):
            self.id = DomainAssignmentStatementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class UnpublishedCitation(Citation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unpublished_Citation
    class_class_curie: ClassVar[str] = "upcore:Unpublished_Citation"
    class_name: ClassVar[str] = "Unpublished_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UnpublishedCitation

    id: Union[str, UnpublishedCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnpublishedCitationId):
            self.id = UnpublishedCitationId(self.id)

        super().__post_init__(**kwargs)


class ActivityRegulationAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Activity_Regulation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Activity_Regulation_Annotation"
    class_name: ClassVar[str] = "Activity_Regulation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ActivityRegulationAnnotation


@dataclass
class Orientation(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Orientation
    class_class_curie: ClassVar[str] = "upcore:Orientation"
    class_name: ClassVar[str] = "Orientation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Orientation

    id: Union[str, OrientationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrientationId):
            self.id = OrientationId(self.id)

        super().__post_init__(**kwargs)


class ReferenceProteome(Proteome):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reference_Proteome
    class_class_curie: ClassVar[str] = "upcore:Reference_Proteome"
    class_name: ClassVar[str] = "Reference_Proteome"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ReferenceProteome


class InductionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Induction_Annotation
    class_class_curie: ClassVar[str] = "upcore:Induction_Annotation"
    class_name: ClassVar[str] = "Induction_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.InductionAnnotation


class SequenceCautionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Caution_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Caution_Annotation"
    class_name: ClassVar[str] = "Sequence_Caution_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SequenceCautionAnnotation


class ErroneousTerminationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Termination_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Termination_Annotation"
    class_name: ClassVar[str] = "Erroneous_Termination_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ErroneousTerminationAnnotation


class SequenceAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Annotation"
    class_name: ClassVar[str] = "Sequence_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SequenceAnnotation


class NaturalVariationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Natural_Variation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Natural_Variation_Annotation"
    class_name: ClassVar[str] = "Natural_Variation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NaturalVariationAnnotation


class CautionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Caution_Annotation
    class_class_curie: ClassVar[str] = "upcore:Caution_Annotation"
    class_name: ClassVar[str] = "Caution_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CautionAnnotation


class ExperimentalInformationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Experimental_Information_Annotation
    class_class_curie: ClassVar[str] = "upcore:Experimental_Information_Annotation"
    class_name: ClassVar[str] = "Experimental_Information_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ExperimentalInformationAnnotation


@dataclass
class NotObsoleteTaxon(Taxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete_Taxon
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete_Taxon"
    class_name: ClassVar[str] = "Not_Obsolete_Taxon"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NotObsoleteTaxon

    id: Union[str, NotObsoleteTaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotObsoleteTaxonId):
            self.id = NotObsoleteTaxonId(self.id)

        super().__post_init__(**kwargs)


class SequenceConflictAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Conflict_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Conflict_Annotation"
    class_name: ClassVar[str] = "Sequence_Conflict_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SequenceConflictAnnotation


@dataclass
class ObservationCitation(UnpublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Observation_Citation
    class_class_curie: ClassVar[str] = "upcore:Observation_Citation"
    class_name: ClassVar[str] = "Observation_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ObservationCitation

    id: Union[str, ObservationCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservationCitationId):
            self.id = ObservationCitationId(self.id)

        super().__post_init__(**kwargs)


class DNA(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.DNA
    class_class_curie: ClassVar[str] = "upcore:DNA"
    class_name: ClassVar[str] = "DNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DNA


class GenomicDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Genomic_DNA
    class_class_curie: ClassVar[str] = "upcore:Genomic_DNA"
    class_name: ClassVar[str] = "Genomic_DNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GenomicDNA


@dataclass
class CitationStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Citation_Statement
    class_class_curie: ClassVar[str] = "upcore:Citation_Statement"
    class_name: ClassVar[str] = "Citation_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CitationStatement

    id: Union[str, CitationStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitationStatementId):
            self.id = CitationStatementId(self.id)

        super().__post_init__(**kwargs)


class RNAEditingAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.RNA_Editing_Annotation
    class_class_curie: ClassVar[str] = "upcore:RNA_Editing_Annotation"
    class_name: ClassVar[str] = "RNA_Editing_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RNAEditingAnnotation


@dataclass
class Part(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Part
    class_class_curie: ClassVar[str] = "upcore:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Part

    id: Union[str, PartId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PartId):
            self.id = PartId(self.id)

        super().__post_init__(**kwargs)


class UnassignedDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unassigned_DNA
    class_class_curie: ClassVar[str] = "upcore:Unassigned_DNA"
    class_name: ClassVar[str] = "Unassigned_DNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UnassignedDNA


class ReviewedProtein(Reviewed):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reviewed_Protein
    class_class_curie: ClassVar[str] = "upcore:Reviewed_Protein"
    class_name: ClassVar[str] = "Reviewed_Protein"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ReviewedProtein


class MassMeasurementMethod(Method):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mass_Measurement_Method
    class_class_curie: ClassVar[str] = "upcore:Mass_Measurement_Method"
    class_name: ClassVar[str] = "Mass_Measurement_Method"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MassMeasurementMethod


class NucleotideResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Resource
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Resource"
    class_name: ClassVar[str] = "Nucleotide_Resource"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NucleotideResource


class PTMAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.PTM_Annotation
    class_class_curie: ClassVar[str] = "upcore:PTM_Annotation"
    class_name: ClassVar[str] = "PTM_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PTMAnnotation


class CofactorAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cofactor_Annotation
    class_class_curie: ClassVar[str] = "upcore:Cofactor_Annotation"
    class_name: ClassVar[str] = "Cofactor_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CofactorAnnotation


class FrameshiftAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Frameshift_Annotation
    class_class_curie: ClassVar[str] = "upcore:Frameshift_Annotation"
    class_name: ClassVar[str] = "Frameshift_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.FrameshiftAnnotation


class PathwayAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pathway_Annotation
    class_class_curie: ClassVar[str] = "upcore:Pathway_Annotation"
    class_name: ClassVar[str] = "Pathway_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PathwayAnnotation


class PolymorphismAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Polymorphism_Annotation
    class_class_curie: ClassVar[str] = "upcore:Polymorphism_Annotation"
    class_name: ClassVar[str] = "Polymorphism_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PolymorphismAnnotation


class NonTerminalResidueAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-terminal_Residue_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-terminal_Residue_Annotation"
    class_name: ClassVar[str] = "Non_terminal_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NonTerminalResidueAnnotation


class ErroneousGeneModelPredictionAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Gene_Model_Prediction_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Gene_Model_Prediction_Annotation"
    class_name: ClassVar[str] = "Erroneous_Gene_Model_Prediction_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ErroneousGeneModelPredictionAnnotation


class MoleculeProcessingAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Molecule_Processing_Annotation
    class_class_curie: ClassVar[str] = "upcore:Molecule_Processing_Annotation"
    class_name: ClassVar[str] = "Molecule_Processing_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MoleculeProcessingAnnotation


class TransitPeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transit_Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Transit_Peptide_Annotation"
    class_name: ClassVar[str] = "Transit_Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TransitPeptideAnnotation


class SignalPeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Signal_Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Signal_Peptide_Annotation"
    class_name: ClassVar[str] = "Signal_Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SignalPeptideAnnotation


class SubunitAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subunit_Annotation
    class_class_curie: ClassVar[str] = "upcore:Subunit_Annotation"
    class_name: ClassVar[str] = "Subunit_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubunitAnnotation


class PeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Peptide_Annotation"
    class_name: ClassVar[str] = "Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PeptideAnnotation


class ErroneousInitiationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Initiation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Initiation_Annotation"
    class_name: ClassVar[str] = "Erroneous_Initiation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ErroneousInitiationAnnotation


class BiotechnologyAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Biotechnology_Annotation
    class_class_curie: ClassVar[str] = "upcore:Biotechnology_Annotation"
    class_name: ClassVar[str] = "Biotechnology_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BiotechnologyAnnotation


class RegionAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Region_Annotation
    class_class_curie: ClassVar[str] = "upcore:Region_Annotation"
    class_name: ClassVar[str] = "Region_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RegionAnnotation


class IntramembraneAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Intramembrane_Annotation
    class_class_curie: ClassVar[str] = "upcore:Intramembrane_Annotation"
    class_name: ClassVar[str] = "Intramembrane_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.IntramembraneAnnotation


class CompositionalBiasAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Compositional_Bias_Annotation
    class_class_curie: ClassVar[str] = "upcore:Compositional_Bias_Annotation"
    class_name: ClassVar[str] = "Compositional_Bias_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CompositionalBiasAnnotation


class TransmembraneAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transmembrane_Annotation
    class_class_curie: ClassVar[str] = "upcore:Transmembrane_Annotation"
    class_name: ClassVar[str] = "Transmembrane_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TransmembraneAnnotation


class CalciumBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Calcium_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Calcium_Binding_Annotation"
    class_name: ClassVar[str] = "Calcium_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CalciumBindingAnnotation


class ZincFingerAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Zinc_Finger_Annotation
    class_class_curie: ClassVar[str] = "upcore:Zinc_Finger_Annotation"
    class_name: ClassVar[str] = "Zinc_Finger_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ZincFingerAnnotation


class CoiledCoilAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Coiled_Coil_Annotation
    class_class_curie: ClassVar[str] = "upcore:Coiled_Coil_Annotation"
    class_name: ClassVar[str] = "Coiled_Coil_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CoiledCoilAnnotation


class RepeatAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Repeat_Annotation
    class_class_curie: ClassVar[str] = "upcore:Repeat_Annotation"
    class_name: ClassVar[str] = "Repeat_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RepeatAnnotation


@dataclass
class NotObsoleteProtein(Protein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete_Protein
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete_Protein"
    class_name: ClassVar[str] = "Not_Obsolete_Protein"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NotObsoleteProtein

    id: Union[str, NotObsoleteProteinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotObsoleteProteinId):
            self.id = NotObsoleteProteinId(self.id)

        super().__post_init__(**kwargs)


class CatalyticActivityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Catalytic_Activity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Catalytic_Activity_Annotation"
    class_name: ClassVar[str] = "Catalytic_Activity_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CatalyticActivityAnnotation


class NonSelfInteraction(Interaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Non_Self_Interaction
    class_class_curie: ClassVar[str] = "upcore:Non_Self_Interaction"
    class_name: ClassVar[str] = "Non_Self_Interaction"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NonSelfInteraction


class KnownSequence(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Known_Sequence
    class_class_curie: ClassVar[str] = "upcore:Known_Sequence"
    class_name: ClassVar[str] = "Known_Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.KnownSequence


class ExternalSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.External_Sequence
    class_class_curie: ClassVar[str] = "upcore:External_Sequence"
    class_name: ClassVar[str] = "External_Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ExternalSequence


class ErroneousTranslationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Translation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Translation_Annotation"
    class_name: ClassVar[str] = "Erroneous_Translation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ErroneousTranslationAnnotation


@dataclass
class StructureMappingStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Mapping_Statement
    class_class_curie: ClassVar[str] = "upcore:Structure_Mapping_Statement"
    class_name: ClassVar[str] = "Structure_Mapping_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.StructureMappingStatement

    id: Union[str, StructureMappingStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StructureMappingStatementId):
            self.id = StructureMappingStatementId(self.id)

        super().__post_init__(**kwargs)


class DevelopmentalStageAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Developmental_Stage_Annotation
    class_class_curie: ClassVar[str] = "upcore:Developmental_Stage_Annotation"
    class_name: ClassVar[str] = "Developmental_Stage_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DevelopmentalStageAnnotation


class SiteAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Site_Annotation"
    class_name: ClassVar[str] = "Site_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SiteAnnotation


class MetalBindingAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Metal_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Metal_Binding_Annotation"
    class_name: ClassVar[str] = "Metal_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MetalBindingAnnotation


class BindingSiteAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Binding_Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Binding_Site_Annotation"
    class_name: ClassVar[str] = "Binding_Site_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BindingSiteAnnotation


class ToxicDoseAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Toxic_Dose_Annotation
    class_class_curie: ClassVar[str] = "upcore:Toxic_Dose_Annotation"
    class_name: ClassVar[str] = "Toxic_Dose_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ToxicDoseAnnotation


class NucleotideBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Binding_Annotation"
    class_name: ClassVar[str] = "Nucleotide_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NucleotideBindingAnnotation


@dataclass
class ObsoleteTaxon(Taxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete_Taxon
    class_class_curie: ClassVar[str] = "upcore:Obsolete_Taxon"
    class_name: ClassVar[str] = "Obsolete_Taxon"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ObsoleteTaxon

    id: Union[str, ObsoleteTaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObsoleteTaxonId):
            self.id = ObsoleteTaxonId(self.id)

        super().__post_init__(**kwargs)


class SecondaryStructureAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Secondary_Structure_Annotation
    class_class_curie: ClassVar[str] = "upcore:Secondary_Structure_Annotation"
    class_name: ClassVar[str] = "Secondary_Structure_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SecondaryStructureAnnotation


class BetaStrandAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Beta_Strand_Annotation
    class_class_curie: ClassVar[str] = "upcore:Beta_Strand_Annotation"
    class_name: ClassVar[str] = "Beta_Strand_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BetaStrandAnnotation


class MutagenesisAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mutagenesis_Annotation
    class_class_curie: ClassVar[str] = "upcore:Mutagenesis_Annotation"
    class_name: ClassVar[str] = "Mutagenesis_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MutagenesisAnnotation


class PharmaceuticalAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pharmaceutical_Annotation
    class_class_curie: ClassVar[str] = "upcore:Pharmaceutical_Annotation"
    class_name: ClassVar[str] = "Pharmaceutical_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PharmaceuticalAnnotation


class RepresentativeProteome(Proteome):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Representative_Proteome
    class_class_curie: ClassVar[str] = "upcore:Representative_Proteome"
    class_name: ClassVar[str] = "Representative_Proteome"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RepresentativeProteome


class NonAdjacentResiduesAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-adjacent_Residues_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-adjacent_Residues_Annotation"
    class_name: ClassVar[str] = "Non_adjacent_Residues_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NonAdjacentResiduesAnnotation


@dataclass
class Concept(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Concept
    class_class_curie: ClassVar[str] = "upcore:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Concept

    id: Union[str, ConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Topology(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Topology
    class_class_curie: ClassVar[str] = "upcore:Topology"
    class_name: ClassVar[str] = "Topology"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Topology

    id: Union[str, TopologyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TopologyId):
            self.id = TopologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObsoleteProtein(Protein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete_Protein
    class_class_curie: ClassVar[str] = "upcore:Obsolete_Protein"
    class_name: ClassVar[str] = "Obsolete_Protein"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ObsoleteProtein

    id: Union[str, ObsoleteProteinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObsoleteProteinId):
            self.id = ObsoleteProteinId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MemberOfRedudantProteome(ObsoleteProtein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Member_Of_Redudant_Proteome
    class_class_curie: ClassVar[str] = "upcore:Member_Of_Redudant_Proteome"
    class_name: ClassVar[str] = "Member_Of_Redudant_Proteome"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MemberOfRedudantProteome

    id: Union[str, MemberOfRedudantProteomeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemberOfRedudantProteomeId):
            self.id = MemberOfRedudantProteomeId(self.id)

        super().__post_init__(**kwargs)


class SimpleSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Simple_Sequence
    class_class_curie: ClassVar[str] = "upcore:Simple_Sequence"
    class_name: ClassVar[str] = "Simple_Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SimpleSequence


@dataclass
class Journal(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Journal
    class_class_curie: ClassVar[str] = "upcore:Journal"
    class_name: ClassVar[str] = "Journal"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Journal

    id: Union[str, JournalId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalId):
            self.id = JournalId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PublishedCitation(Citation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Published_Citation
    class_class_curie: ClassVar[str] = "upcore:Published_Citation"
    class_name: ClassVar[str] = "Published_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PublishedCitation

    id: Union[str, PublishedCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublishedCitationId):
            self.id = PublishedCitationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SubmissionCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Submission_Citation
    class_class_curie: ClassVar[str] = "upcore:Submission_Citation"
    class_name: ClassVar[str] = "Submission_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubmissionCitation

    id: Union[str, SubmissionCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubmissionCitationId):
            self.id = SubmissionCitationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class JournalCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Journal_Citation
    class_class_curie: ClassVar[str] = "upcore:Journal_Citation"
    class_name: ClassVar[str] = "Journal_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.JournalCitation

    id: Union[str, JournalCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalCitationId):
            self.id = JournalCitationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PatentCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Patent_Citation
    class_class_curie: ClassVar[str] = "upcore:Patent_Citation"
    class_name: ClassVar[str] = "Patent_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PatentCitation

    id: Union[str, PatentCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatentCitationId):
            self.id = PatentCitationId(self.id)

        super().__post_init__(**kwargs)


class MassSpectrometryAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mass_Spectrometry_Annotation
    class_class_curie: ClassVar[str] = "upcore:Mass_Spectrometry_Annotation"
    class_name: ClassVar[str] = "Mass_Spectrometry_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MassSpectrometryAnnotation


@dataclass
class BookCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Book_Citation
    class_class_curie: ClassVar[str] = "upcore:Book_Citation"
    class_name: ClassVar[str] = "Book_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BookCitation

    id: Union[str, BookCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookCitationId):
            self.id = BookCitationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CellularComponent(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cellular_Component
    class_class_curie: ClassVar[str] = "upcore:Cellular_Component"
    class_name: ClassVar[str] = "Cellular_Component"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CellularComponent

    id: Union[str, CellularComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)

        super().__post_init__(**kwargs)


class NaturalVariantAnnotation(NaturalVariationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Natural_Variant_Annotation
    class_class_curie: ClassVar[str] = "upcore:Natural_Variant_Annotation"
    class_name: ClassVar[str] = "Natural_Variant_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NaturalVariantAnnotation


class StructureResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Resource
    class_class_curie: ClassVar[str] = "upcore:Structure_Resource"
    class_name: ClassVar[str] = "Structure_Resource"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.StructureResource


class UnknownSequence(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unknown_Sequence
    class_class_curie: ClassVar[str] = "upcore:Unknown_Sequence"
    class_name: ClassVar[str] = "Unknown_Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UnknownSequence


class AlternativeSequenceAnnotation(NaturalVariationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Sequence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Sequence_Annotation"
    class_name: ClassVar[str] = "Alternative_Sequence_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AlternativeSequenceAnnotation


class ActiveSiteAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Active_Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Active_Site_Annotation"
    class_name: ClassVar[str] = "Active_Site_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ActiveSiteAnnotation


@dataclass
class NucleotideMappingStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Mapping_Statement
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Mapping_Statement"
    class_name: ClassVar[str] = "Nucleotide_Mapping_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NucleotideMappingStatement

    id: Union[str, NucleotideMappingStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleotideMappingStatementId):
            self.id = NucleotideMappingStatementId(self.id)

        super().__post_init__(**kwargs)


class ModificationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modification_Annotation
    class_class_curie: ClassVar[str] = "upcore:Modification_Annotation"
    class_name: ClassVar[str] = "Modification_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ModificationAnnotation


class LipidationAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Lipidation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Lipidation_Annotation"
    class_name: ClassVar[str] = "Lipidation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.LipidationAnnotation


class ModifiedResidueAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modified_Residue_Annotation
    class_class_curie: ClassVar[str] = "upcore:Modified_Residue_Annotation"
    class_name: ClassVar[str] = "Modified_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ModifiedResidueAnnotation


class GlycosylationAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Glycosylation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Glycosylation_Annotation"
    class_name: ClassVar[str] = "Glycosylation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GlycosylationAnnotation


class InitiatorMethionineAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Initiator_Methionine_Annotation
    class_class_curie: ClassVar[str] = "upcore:Initiator_Methionine_Annotation"
    class_name: ClassVar[str] = "Initiator_Methionine_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.InitiatorMethionineAnnotation


class MotifAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Motif_Annotation
    class_class_curie: ClassVar[str] = "upcore:Motif_Annotation"
    class_name: ClassVar[str] = "Motif_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MotifAnnotation


class SimilarityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Similarity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Similarity_Annotation"
    class_name: ClassVar[str] = "Similarity_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SimilarityAnnotation


@dataclass
class Database(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Database
    class_class_curie: ClassVar[str] = "upcore:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Database

    id: Union[str, DatabaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseId):
            self.id = DatabaseId(self.id)

        super().__post_init__(**kwargs)


class NPBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.NP_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:NP_Binding_Annotation"
    class_name: ClassVar[str] = "NP_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NPBindingAnnotation


class TopologicalDomainAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Topological_Domain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Topological_Domain_Annotation"
    class_name: ClassVar[str] = "Topological_Domain_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TopologicalDomainAnnotation


class TissueSpecificityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Tissue_Specificity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Tissue_Specificity_Annotation"
    class_name: ClassVar[str] = "Tissue_Specificity_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TissueSpecificityAnnotation


class TranscriptResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transcript_Resource
    class_class_curie: ClassVar[str] = "upcore:Transcript_Resource"
    class_name: ClassVar[str] = "Transcript_Resource"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TranscriptResource


class FunctionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Function_Annotation
    class_class_curie: ClassVar[str] = "upcore:Function_Annotation"
    class_name: ClassVar[str] = "Function_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.FunctionAnnotation


@dataclass
class EndpointStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Endpoint_Statement
    class_class_curie: ClassVar[str] = "upcore:Endpoint_Statement"
    class_name: ClassVar[str] = "Endpoint_Statement"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.EndpointStatement

    id: Union[str, EndpointStatementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EndpointStatementId):
            self.id = EndpointStatementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProteomeComponent(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Proteome_Component
    class_class_curie: ClassVar[str] = "upcore:Proteome_Component"
    class_name: ClassVar[str] = "Proteome_Component"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ProteomeComponent

    id: Union[str, ProteomeComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteomeComponentId):
            self.id = ProteomeComponentId(self.id)

        super().__post_init__(**kwargs)


class CrossLinkAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Cross-link_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Cross-link_Annotation"
    class_name: ClassVar[str] = "Cross_link_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.CrossLinkAnnotation


class StructureDeterminationMethod(Method):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Determination_Method
    class_class_curie: ClassVar[str] = "upcore:Structure_Determination_Method"
    class_name: ClassVar[str] = "Structure_Determination_Method"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.StructureDeterminationMethod


class DisulfideBondAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disulfide_Bond_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disulfide_Bond_Annotation"
    class_name: ClassVar[str] = "Disulfide_Bond_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DisulfideBondAnnotation


class BiophysicochemicalAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Biophysicochemical_Annotation
    class_class_curie: ClassVar[str] = "upcore:Biophysicochemical_Annotation"
    class_name: ClassVar[str] = "Biophysicochemical_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.BiophysicochemicalAnnotation


class TemperatureDependenceAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Temperature_Dependence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Temperature_Dependence_Annotation"
    class_name: ClassVar[str] = "Temperature_Dependence_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TemperatureDependenceAnnotation


class RedoxPotentialAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Redox_Potential_Annotation
    class_class_curie: ClassVar[str] = "upcore:Redox_Potential_Annotation"
    class_name: ClassVar[str] = "Redox_Potential_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RedoxPotentialAnnotation


class PHDependenceAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.PH_Dependence_Annotation
    class_class_curie: ClassVar[str] = "upcore:PH_Dependence_Annotation"
    class_name: ClassVar[str] = "PH_Dependence_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PHDependenceAnnotation


class KineticsAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Kinetics_Annotation
    class_class_curie: ClassVar[str] = "upcore:Kinetics_Annotation"
    class_name: ClassVar[str] = "Kinetics_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.KineticsAnnotation


class DomainExtentAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Extent_Annotation
    class_class_curie: ClassVar[str] = "upcore:Domain_Extent_Annotation"
    class_name: ClassVar[str] = "Domain_Extent_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DomainExtentAnnotation


class SequenceUncertaintyAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Uncertainty_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Uncertainty_Annotation"
    class_name: ClassVar[str] = "Sequence_Uncertainty_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SequenceUncertaintyAnnotation


class DiseaseAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disease_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disease_Annotation"
    class_name: ClassVar[str] = "Disease_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DiseaseAnnotation


@dataclass
class ElectronicCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Electronic_Citation
    class_class_curie: ClassVar[str] = "upcore:Electronic_Citation"
    class_name: ClassVar[str] = "Electronic_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ElectronicCitation

    id: Union[str, ElectronicCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElectronicCitationId):
            self.id = ElectronicCitationId(self.id)

        super().__post_init__(**kwargs)


class TurnAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Turn_Annotation
    class_class_curie: ClassVar[str] = "upcore:Turn_Annotation"
    class_name: ClassVar[str] = "Turn_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TurnAnnotation


class SelfInteraction(Interaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Self_Interaction
    class_class_curie: ClassVar[str] = "upcore:Self_Interaction"
    class_name: ClassVar[str] = "Self_Interaction"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SelfInteraction


class DomainAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Domain_Annotation"
    class_name: ClassVar[str] = "Domain_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DomainAnnotation


class ChainAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Chain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Chain_Annotation"
    class_name: ClassVar[str] = "Chain_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ChainAnnotation


class SubcellularLocationAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subcellular_Location_Annotation
    class_class_curie: ClassVar[str] = "upcore:Subcellular_Location_Annotation"
    class_name: ClassVar[str] = "Subcellular_Location_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.SubcellularLocationAnnotation


class DisruptionPhenotypeAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disruption_Phenotype_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disruption_Phenotype_Annotation"
    class_name: ClassVar[str] = "Disruption_Phenotype_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DisruptionPhenotypeAnnotation


@dataclass
class ThesisCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Thesis_Citation
    class_class_curie: ClassVar[str] = "upcore:Thesis_Citation"
    class_name: ClassVar[str] = "Thesis_Citation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ThesisCitation

    id: Union[str, ThesisCitationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThesisCitationId):
            self.id = ThesisCitationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cluster(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cluster
    class_class_curie: ClassVar[str] = "upcore:Cluster"
    class_name: ClassVar[str] = "Cluster"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Cluster

    id: Union[str, ClusterId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClusterId):
            self.id = ClusterId(self.id)

        super().__post_init__(**kwargs)


class RNA(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.RNA
    class_class_curie: ClassVar[str] = "upcore:RNA"
    class_name: ClassVar[str] = "RNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RNA


class OtherRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Other_RNA
    class_class_curie: ClassVar[str] = "upcore:Other_RNA"
    class_name: ClassVar[str] = "Other_RNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OtherRNA


class UnassignedRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unassigned_RNA
    class_class_curie: ClassVar[str] = "upcore:Unassigned_RNA"
    class_name: ClassVar[str] = "Unassigned_RNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UnassignedRNA


class ViralCRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Viral_cRNA
    class_class_curie: ClassVar[str] = "upcore:Viral_cRNA"
    class_name: ClassVar[str] = "Viral_cRNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ViralCRNA


class GenomicRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Genomic_RNA
    class_class_curie: ClassVar[str] = "upcore:Genomic_RNA"
    class_name: ClassVar[str] = "Genomic_RNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GenomicRNA


class TranscribedRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transcribed_RNA
    class_class_curie: ClassVar[str] = "upcore:Transcribed_RNA"
    class_name: ClassVar[str] = "Transcribed_RNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.TranscribedRNA


class MRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.MRNA
    class_class_curie: ClassVar[str] = "upcore:MRNA"
    class_name: ClassVar[str] = "MRNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.MRNA


class AbsorptionAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Absorption_Annotation
    class_class_curie: ClassVar[str] = "upcore:Absorption_Annotation"
    class_name: ClassVar[str] = "Absorption_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AbsorptionAnnotation


class OtherDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Other_DNA
    class_class_curie: ClassVar[str] = "upcore:Other_DNA"
    class_name: ClassVar[str] = "Other_DNA"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OtherDNA


class ModifiedSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modified_Sequence
    class_class_curie: ClassVar[str] = "upcore:Modified_Sequence"
    class_name: ClassVar[str] = "Modified_Sequence"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ModifiedSequence


class AllergenAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Allergen_Annotation
    class_class_curie: ClassVar[str] = "upcore:Allergen_Annotation"
    class_name: ClassVar[str] = "Allergen_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AllergenAnnotation


class NonStandardResidueAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-standard_Residue_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-standard_Residue_Annotation"
    class_name: ClassVar[str] = "Non_standard_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.NonStandardResidueAnnotation


class PropeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Propeptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Propeptide_Annotation"
    class_name: ClassVar[str] = "Propeptide_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PropeptideAnnotation


@dataclass
class Gene(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Gene
    class_class_curie: ClassVar[str] = "upcore:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Gene

    id: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        super().__post_init__(**kwargs)


class HelixAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Helix_Annotation
    class_class_curie: ClassVar[str] = "upcore:Helix_Annotation"
    class_name: ClassVar[str] = "Helix_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.HelixAnnotation


class AlternativeProductsAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Products_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Products_Annotation"
    class_name: ClassVar[str] = "Alternative_Products_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AlternativeProductsAnnotation


class AlternativePromoterUsageAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Promoter_Usage_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Promoter_Usage_Annotation"
    class_name: ClassVar[str] = "Alternative_Promoter_Usage_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AlternativePromoterUsageAnnotation


class RibosomalFrameshifting(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Ribosomal_Frameshifting
    class_class_curie: ClassVar[str] = "upcore:Ribosomal_Frameshifting"
    class_name: ClassVar[str] = "Ribosomal_Frameshifting"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.RibosomalFrameshifting


class AlternativeSplicingAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Splicing_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Splicing_Annotation"
    class_name: ClassVar[str] = "Alternative_Splicing_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AlternativeSplicingAnnotation


class AlternativeInitiationAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Initiation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Initiation_Annotation"
    class_name: ClassVar[str] = "Alternative_Initiation_Annotation"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.AlternativeInitiationAnnotation


# Enumerations
class UberGraphSourceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="UberGraphSourceEnum",
    )

class BloodVesselSubcategory(EnumDefinitionImpl):

    artery = PermissibleValue(text="artery",
                                   meaning=UBERON["0001637"])
    vein = PermissibleValue(text="vein",
                               meaning=UBERON["0001638"])

    _defn = EnumDefinition(
        name="BloodVesselSubcategory",
    )

# Slots
class slots:
    pass

slots.results = Slot(uri=RESULTSET.results, name="results", curie=RESULTSET.curie('results'),
                   model_uri=SPARQLFUN.results, domain=None, range=Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]])

slots.binding_key = Slot(uri=RESULTSET.binding_key, name="binding_key", curie=RESULTSET.curie('binding_key'),
                   model_uri=SPARQLFUN.binding_key, domain=None, range=URIRef)

slots.binding_value = Slot(uri=RESULTSET.binding_value, name="binding_value", curie=RESULTSET.curie('binding_value'),
                   model_uri=SPARQLFUN.binding_value, domain=None, range=Optional[str])

slots.query_template = Slot(uri=RESULTSET.query_template, name="query_template", curie=RESULTSET.curie('query_template'),
                   model_uri=SPARQLFUN.query_template, domain=None, range=Optional[str])

slots.bindings = Slot(uri=RESULTSET.bindings, name="bindings", curie=RESULTSET.curie('bindings'),
                   model_uri=SPARQLFUN.bindings, domain=None, range=Optional[Union[Dict[Union[str, BindingBindingKey], Union[dict, Binding]], List[Union[dict, Binding]]]])

slots.id = Slot(uri=SPARQLFUN_RDF.id, name="id", curie=SPARQLFUN_RDF.curie('id'),
                   model_uri=SPARQLFUN.id, domain=None, range=URIRef)

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.subject, domain=None, range=Optional[Union[str, NodeId]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=SPARQLFUN.predicate, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.object, domain=None, range=Optional[Union[dict, NodeOrLiteral]])

slots.value_object = Slot(uri=SPARQLFUN_RDF.value_object, name="value_object", curie=SPARQLFUN_RDF.curie('value_object'),
                   model_uri=SPARQLFUN.value_object, domain=None, range=Optional[str])

slots.node_object = Slot(uri=SPARQLFUN_RDF.node_object, name="node_object", curie=SPARQLFUN_RDF.curie('node_object'),
                   model_uri=SPARQLFUN.node_object, domain=None, range=Optional[Union[str, NodeId]])

slots.graph = Slot(uri=RDFS.isDefinedBy, name="graph", curie=RDFS.curie('isDefinedBy'),
                   model_uri=SPARQLFUN.graph, domain=None, range=Optional[Union[str, NodeId]])

slots.statements = Slot(uri=SPARQLFUN.statements, name="statements", curie=SPARQLFUN.curie('statements'),
                   model_uri=SPARQLFUN.statements, domain=None, range=Optional[Union[Union[dict, Statement], List[Union[dict, Statement]]]])

slots.value_statements = Slot(uri=SPARQLFUN.value_statements, name="value_statements", curie=SPARQLFUN.curie('value_statements'),
                   model_uri=SPARQLFUN.value_statements, domain=None, range=Optional[Union[Union[dict, NodeToValueStatement], List[Union[dict, NodeToValueStatement]]]])

slots.node_statements = Slot(uri=SPARQLFUN.node_statements, name="node_statements", curie=SPARQLFUN.curie('node_statements'),
                   model_uri=SPARQLFUN.node_statements, domain=None, range=Optional[Union[Union[dict, NodeToNodeStatement], List[Union[dict, NodeToNodeStatement]]]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=SPARQLFUN.type, domain=None, range=Optional[Union[str, NodeId]])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=SPARQLFUN.label, domain=None, range=Optional[str])

slots.category = Slot(uri=SPARQLFUN_RDF.category, name="category", curie=SPARQLFUN_RDF.curie('category'),
                   model_uri=SPARQLFUN.category, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.datatype = Slot(uri=SPARQLFUN_RDF.datatype, name="datatype", curie=SPARQLFUN_RDF.curie('datatype'),
                   model_uri=SPARQLFUN.datatype, domain=None, range=Optional[Union[str, NodeId]])

slots.value = Slot(uri=SPARQLFUN_RDF.value, name="value", curie=SPARQLFUN_RDF.curie('value'),
                   model_uri=SPARQLFUN.value, domain=None, range=Optional[Union[str, LiteralAsStringType]])

slots.language = Slot(uri=SPARQLFUN_RDF.language, name="language", curie=SPARQLFUN_RDF.curie('language'),
                   model_uri=SPARQLFUN.language, domain=None, range=Optional[str])

slots.prefix = Slot(uri=SH.prefix, name="prefix", curie=SH.curie('prefix'),
                   model_uri=SPARQLFUN.prefix, domain=None, range=Optional[Union[str, NCName]])

slots.base = Slot(uri=SH.namespace, name="base", curie=SH.curie('namespace'),
                   model_uri=SPARQLFUN.base, domain=None, range=Optional[Union[str, URI]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=SPARQLFUN.description, domain=None, range=Optional[Union[str, NodeId]])

slots.regex_slot = Slot(uri=SPARQLFUN_RDF.regex_slot, name="regex_slot", curie=SPARQLFUN_RDF.curie('regex_slot'),
                   model_uri=SPARQLFUN.regex_slot, domain=None, range=Optional[str])

slots.class1 = Slot(uri=SPARQLFUN_OWL.class1, name="class1", curie=SPARQLFUN_OWL.curie('class1'),
                   model_uri=SPARQLFUN.class1, domain=None, range=Optional[Union[str, NodeId]])

slots.class2 = Slot(uri=SPARQLFUN_OWL.class2, name="class2", curie=SPARQLFUN_OWL.curie('class2'),
                   model_uri=SPARQLFUN.class2, domain=None, range=Optional[Union[str, NodeId]])

slots.descendant_class = Slot(uri=SPARQLFUN_OWL.descendant_class, name="descendant_class", curie=SPARQLFUN_OWL.curie('descendant_class'),
                   model_uri=SPARQLFUN.descendant_class, domain=None, range=Optional[Union[str, NodeId]])

slots.axiom_identifier = Slot(uri=SPARQLFUN_OWL.axiom_identifier, name="axiom_identifier", curie=SPARQLFUN_OWL.curie('axiom_identifier'),
                   model_uri=SPARQLFUN.axiom_identifier, domain=None, range=Optional[Union[str, BlankNodeId]])

slots.filler = Slot(uri=SPARQLFUN_OWL.filler, name="filler", curie=SPARQLFUN_OWL.curie('filler'),
                   model_uri=SPARQLFUN.filler, domain=None, range=Optional[Union[str, NodeId]])

slots.axiom_predicate = Slot(uri=SPARQLFUN_OWL.axiom_predicate, name="axiom_predicate", curie=SPARQLFUN_OWL.curie('axiom_predicate'),
                   model_uri=SPARQLFUN.axiom_predicate, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.axiom_object = Slot(uri=SPARQLFUN_OWL.axiom_object, name="axiom_object", curie=SPARQLFUN_OWL.curie('axiom_object'),
                   model_uri=SPARQLFUN.axiom_object, domain=None, range=Optional[Union[dict, NodeOrLiteral]])

slots.annotations = Slot(uri=SPARQLFUN_OWL.annotations, name="annotations", curie=SPARQLFUN_OWL.curie('annotations'),
                   model_uri=SPARQLFUN.annotations, domain=None, range=Optional[Union[dict, OwlAnnotation]])

slots.label_regex = Slot(uri=SPARQLFUN_OMO.label_regex, name="label_regex", curie=SPARQLFUN_OMO.curie('label_regex'),
                   model_uri=SPARQLFUN.label_regex, domain=None, range=Optional[str])

slots.label_starts_with = Slot(uri=SPARQLFUN_OMO.label_starts_with, name="label_starts_with", curie=SPARQLFUN_OMO.curie('label_starts_with'),
                   model_uri=SPARQLFUN.label_starts_with, domain=None, range=Optional[str])

slots.xxresults = Slot(uri=SPARQLFUN_OMO.xxresults, name="xxresults", curie=SPARQLFUN_OMO.curie('xxresults'),
                   model_uri=SPARQLFUN.xxresults, domain=None, range=Optional[Union[List[Union[str, NodeId]], Dict[Union[str, NodeId], Union[dict, Node]]]])

slots.definition = Slot(uri=IAO['0000115'], name="definition", curie=IAO.curie('0000115'),
                   model_uri=SPARQLFUN.definition, domain=None, range=Optional[str])

slots.exact_synonyms = Slot(uri=OBOINOWL.hasExactSynonym, name="exact_synonyms", curie=OBOINOWL.curie('hasExactSynonym'),
                   model_uri=SPARQLFUN.exact_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.ancestor = Slot(uri=SPARQLFUN_UBERGRAPH.ancestor, name="ancestor", curie=SPARQLFUN_UBERGRAPH.curie('ancestor'),
                   model_uri=SPARQLFUN.ancestor, domain=None, range=Optional[Union[str, NodeId]])

slots.descendant = Slot(uri=SPARQLFUN_UBERGRAPH.descendant, name="descendant", curie=SPARQLFUN_UBERGRAPH.curie('descendant'),
                   model_uri=SPARQLFUN.descendant, domain=None, range=Optional[Union[str, NodeId]])

slots.node1 = Slot(uri=SPARQLFUN_UBERGRAPH.node1, name="node1", curie=SPARQLFUN_UBERGRAPH.curie('node1'),
                   model_uri=SPARQLFUN.node1, domain=None, range=Optional[Union[str, NodeId]])

slots.node2 = Slot(uri=SPARQLFUN_UBERGRAPH.node2, name="node2", curie=SPARQLFUN_UBERGRAPH.curie('node2'),
                   model_uri=SPARQLFUN.node2, domain=None, range=Optional[Union[str, NodeId]])

slots.is_direction_canonical = Slot(uri=SPARQLFUN_UBERGRAPH.is_direction_canonical, name="is_direction_canonical", curie=SPARQLFUN_UBERGRAPH.curie('is_direction_canonical'),
                   model_uri=SPARQLFUN.is_direction_canonical, domain=None, range=Optional[Union[bool, Bool]])

slots.node1_candidates = Slot(uri=SPARQLFUN_UBERGRAPH.node1_candidates, name="node1_candidates", curie=SPARQLFUN_UBERGRAPH.curie('node1_candidates'),
                   model_uri=SPARQLFUN.node1_candidates, domain=None, range=Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]])

slots.node2_candidates = Slot(uri=SPARQLFUN_UBERGRAPH.node2_candidates, name="node2_candidates", curie=SPARQLFUN_UBERGRAPH.curie('node2_candidates'),
                   model_uri=SPARQLFUN.node2_candidates, domain=None, range=Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]])

slots.nodes = Slot(uri=SPARQLFUN_UBERGRAPH.nodes, name="nodes", curie=SPARQLFUN_UBERGRAPH.curie('nodes'),
                   model_uri=SPARQLFUN.nodes, domain=None, range=Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]])

slots.predicate1 = Slot(uri=SPARQLFUN_UBERGRAPH.predicate1, name="predicate1", curie=SPARQLFUN_UBERGRAPH.curie('predicate1'),
                   model_uri=SPARQLFUN.predicate1, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.predicate2 = Slot(uri=SPARQLFUN_UBERGRAPH.predicate2, name="predicate2", curie=SPARQLFUN_UBERGRAPH.curie('predicate2'),
                   model_uri=SPARQLFUN.predicate2, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.subject_predicate = Slot(uri=SPARQLFUN_UBERGRAPH.subject_predicate, name="subject_predicate", curie=SPARQLFUN_UBERGRAPH.curie('subject_predicate'),
                   model_uri=SPARQLFUN.subject_predicate, domain=None, range=Optional[Union[str, NodeId]])

slots.class_with_constraint = Slot(uri=SPARQLFUN_UBERGRAPH.class_with_constraint, name="class_with_constraint", curie=SPARQLFUN_UBERGRAPH.curie('class_with_constraint'),
                   model_uri=SPARQLFUN.class_with_constraint, domain=None, range=Optional[Union[str, NodeId]])

slots.direct_taxon = Slot(uri=SPARQLFUN_UBERGRAPH.direct_taxon, name="direct_taxon", curie=SPARQLFUN_UBERGRAPH.curie('direct_taxon'),
                   model_uri=SPARQLFUN.direct_taxon, domain=None, range=Optional[Union[str, NodeId]])

slots.query_has_subclass_ancestor = Slot(uri=SPARQLFUN_UBERGRAPH.query_has_subclass_ancestor, name="query_has_subclass_ancestor", curie=SPARQLFUN_UBERGRAPH.curie('query_has_subclass_ancestor'),
                   model_uri=SPARQLFUN.query_has_subclass_ancestor, domain=None, range=Optional[Union[str, NodeId]])

slots.subcategory = Slot(uri=SPARQLFUN.subcategory, name="subcategory", curie=SPARQLFUN.curie('subcategory'),
                   model_uri=SPARQLFUN.subcategory, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.supplies = Slot(uri=RO['0002178'], name="supplies", curie=RO.curie('0002178'),
                   model_uri=SPARQLFUN.supplies, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.drains = Slot(uri=RO['0002179'], name="drains", curie=RO.curie('0002179'),
                   model_uri=SPARQLFUN.drains, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.branching_part_of = Slot(uri=RO['0002380'], name="branching_part_of", curie=RO.curie('0002380'),
                   model_uri=SPARQLFUN.branching_part_of, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.subject_category = Slot(uri=SPARQLFUN_BIOLINK.subject_category, name="subject_category", curie=SPARQLFUN_BIOLINK.curie('subject_category'),
                   model_uri=SPARQLFUN.subject_category, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.object_category = Slot(uri=SPARQLFUN_BIOLINK.object_category, name="object_category", curie=SPARQLFUN_BIOLINK.curie('object_category'),
                   model_uri=SPARQLFUN.object_category, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.subject_category_inferred = Slot(uri=SPARQLFUN_BIOLINK.subject_category_inferred, name="subject_category_inferred", curie=SPARQLFUN_BIOLINK.curie('subject_category_inferred'),
                   model_uri=SPARQLFUN.subject_category_inferred, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.object_category_inferred = Slot(uri=SPARQLFUN_BIOLINK.object_category_inferred, name="object_category_inferred", curie=SPARQLFUN_BIOLINK.curie('object_category_inferred'),
                   model_uri=SPARQLFUN.object_category_inferred, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.seeAlso = Slot(uri=RDFS.seeAlso, name="seeAlso", curie=RDFS.curie('seeAlso'),
                   model_uri=SPARQLFUN.seeAlso, domain=None, range=Optional[Union[str, ThingId]])

slots.objectProperty = Slot(uri=UPCORE.objectProperty, name="objectProperty", curie=UPCORE.curie('objectProperty'),
                   model_uri=SPARQLFUN.objectProperty, domain=None, range=Optional[Union[str, NodeId]])

slots.catalyticActivity = Slot(uri=UPCORE.catalyticActivity, name="catalyticActivity", curie=UPCORE.curie('catalyticActivity'),
                   model_uri=SPARQLFUN.catalyticActivity, domain=None, range=Optional[Union[dict, CatalyticActivity]])

slots.mappedAnnotation = Slot(uri=UPCORE.mappedAnnotation, name="mappedAnnotation", curie=UPCORE.curie('mappedAnnotation'),
                   model_uri=SPARQLFUN.mappedAnnotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.structuredName = Slot(uri=UPCORE.structuredName, name="structuredName", curie=UPCORE.curie('structuredName'),
                   model_uri=SPARQLFUN.structuredName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.mappedCitation = Slot(uri=UPCORE.mappedCitation, name="mappedCitation", curie=UPCORE.curie('mappedCitation'),
                   model_uri=SPARQLFUN.mappedCitation, domain=None, range=Optional[Union[str, CitationId]])

slots.topology = Slot(uri=UPCORE.topology, name="topology", curie=UPCORE.curie('topology'),
                   model_uri=SPARQLFUN.topology, domain=None, range=Optional[Union[str, TopologyId]])

slots.classifiedWith = Slot(uri=UPCORE.classifiedWith, name="classifiedWith", curie=UPCORE.curie('classifiedWith'),
                   model_uri=SPARQLFUN.classifiedWith, domain=None, range=Optional[Union[str, ConceptId]])

slots.encodedIn = Slot(uri=UPCORE.encodedIn, name="encodedIn", curie=UPCORE.curie('encodedIn'),
                   model_uri=SPARQLFUN.encodedIn, domain=None, range=Optional[Union[str, SubcellularLocationId]])

slots.potentialSequence = Slot(uri=UPCORE.potentialSequence, name="potentialSequence", curie=UPCORE.curie('potentialSequence'),
                   model_uri=SPARQLFUN.potentialSequence, domain=None, range=Optional[Union[dict, Sequence]])

slots.domain = Slot(uri=UPCORE.domain, name="domain", curie=UPCORE.curie('domain'),
                   model_uri=SPARQLFUN.domain, domain=None, range=Optional[Union[str, PartId]])

slots.enzymeClass = Slot(uri=UPCORE.enzymeClass, name="enzymeClass", curie=UPCORE.curie('enzymeClass'),
                   model_uri=SPARQLFUN.enzymeClass, domain=None, range=Optional[Union[str, EnzymeId]])

slots.publishedIn = Slot(uri=UPCORE.publishedIn, name="publishedIn", curie=UPCORE.curie('publishedIn'),
                   model_uri=SPARQLFUN.publishedIn, domain=None, range=Optional[Union[str, JournalId]])

slots.translatedFrom = Slot(uri=UPCORE.translatedFrom, name="translatedFrom", curie=UPCORE.curie('translatedFrom'),
                   model_uri=SPARQLFUN.translatedFrom, domain=None, range=Optional[Union[dict, NucleotideResource]])

slots.erratumFor = Slot(uri=UPCORE.erratumFor, name="erratumFor", curie=UPCORE.curie('erratumFor'),
                   model_uri=SPARQLFUN.erratumFor, domain=None, range=Optional[Union[str, PublishedCitationId]])

slots.member = Slot(uri=UPCORE.member, name="member", curie=UPCORE.curie('member'),
                   model_uri=SPARQLFUN.member, domain=None, range=Optional[Union[dict, Sequence]])

slots.interaction = Slot(uri=UPCORE.interaction, name="interaction", curie=UPCORE.curie('interaction'),
                   model_uri=SPARQLFUN.interaction, domain=None, range=Optional[Union[dict, Interaction]])

slots.attribution = Slot(uri=UPCORE.attribution, name="attribution", curie=UPCORE.curie('attribution'),
                   model_uri=SPARQLFUN.attribution, domain=None, range=Optional[Union[dict, Attribution]])

slots.erratum = Slot(uri=UPCORE.erratum, name="erratum", curie=UPCORE.curie('erratum'),
                   model_uri=SPARQLFUN.erratum, domain=None, range=Optional[Union[str, PublishedCitationId]])

slots.strain = Slot(uri=UPCORE.strain, name="strain", curie=UPCORE.curie('strain'),
                   model_uri=SPARQLFUN.strain, domain=None, range=Optional[Union[dict, Strain]])

slots.basedOn = Slot(uri=UPCORE.basedOn, name="basedOn", curie=UPCORE.curie('basedOn'),
                   model_uri=SPARQLFUN.basedOn, domain=None, range=Optional[Union[dict, SimpleSequence]])

slots.alternativeName = Slot(uri=UPCORE.alternativeName, name="alternativeName", curie=UPCORE.curie('alternativeName'),
                   model_uri=SPARQLFUN.alternativeName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.orientation = Slot(uri=UPCORE.orientation, name="orientation", curie=UPCORE.curie('orientation'),
                   model_uri=SPARQLFUN.orientation, domain=None, range=Optional[Union[str, OrientationId]])

slots.database = Slot(uri=UPCORE.database, name="database", curie=UPCORE.curie('database'),
                   model_uri=SPARQLFUN.database, domain=None, range=Optional[Union[str, DatabaseId]])

slots.host = Slot(uri=UPCORE.host, name="host", curie=UPCORE.curie('host'),
                   model_uri=SPARQLFUN.host, domain=None, range=Optional[Union[str, TaxonId]])

slots.enzyme = Slot(uri=UPCORE.enzyme, name="enzyme", curie=UPCORE.curie('enzyme'),
                   model_uri=SPARQLFUN.enzyme, domain=None, range=Optional[Union[str, EnzymeId]])

slots.modification = Slot(uri=UPCORE.modification, name="modification", curie=UPCORE.curie('modification'),
                   model_uri=SPARQLFUN.modification, domain=None, range=Optional[Union[dict, AlternativeSequenceAnnotation]])

slots.partOf = Slot(uri=UPCORE.partOf, name="partOf", curie=UPCORE.curie('partOf'),
                   model_uri=SPARQLFUN.partOf, domain=None, range=Optional[Union[str, SubcellularLocationId]])

slots.rank = Slot(uri=UPCORE.rank, name="rank", curie=UPCORE.curie('rank'),
                   model_uri=SPARQLFUN.rank, domain=None, range=Optional[Union[dict, Rank]])

slots.participant = Slot(uri=UPCORE.participant, name="participant", curie=UPCORE.curie('participant'),
                   model_uri=SPARQLFUN.participant, domain=None, range=Optional[Union[dict, Participant]])

slots.activity = Slot(uri=UPCORE.activity, name="activity", curie=UPCORE.curie('activity'),
                   model_uri=SPARQLFUN.activity, domain=None, range=Optional[Union[dict, CatalyticActivity]])

slots.organism = Slot(uri=UPCORE.organism, name="organism", curie=UPCORE.curie('organism'),
                   model_uri=SPARQLFUN.organism, domain=None, range=Optional[Union[str, TaxonId]])

slots.conflictingSequence = Slot(uri=UPCORE.conflictingSequence, name="conflictingSequence", curie=UPCORE.curie('conflictingSequence'),
                   model_uri=SPARQLFUN.conflictingSequence, domain=None, range=Optional[Union[dict, ExternalSequence]])

slots.citation = Slot(uri=UPCORE.citation, name="citation", curie=UPCORE.curie('citation'),
                   model_uri=SPARQLFUN.citation, domain=None, range=Optional[Union[str, CitationId]])

slots.seedFor = Slot(uri=UPCORE.seedFor, name="seedFor", curie=UPCORE.curie('seedFor'),
                   model_uri=SPARQLFUN.seedFor, domain=None, range=Optional[Union[str, ClusterId]])

slots.representativeFor = Slot(uri=UPCORE.representativeFor, name="representativeFor", curie=UPCORE.curie('representativeFor'),
                   model_uri=SPARQLFUN.representativeFor, domain=None, range=Optional[Union[str, ClusterId]])

slots.relatedLocation = Slot(uri=UPCORE.relatedLocation, name="relatedLocation", curie=UPCORE.curie('relatedLocation'),
                   model_uri=SPARQLFUN.relatedLocation, domain=None, range=Optional[Union[str, SubcellularLocationId]])

slots.isolatedFrom = Slot(uri=UPCORE.isolatedFrom, name="isolatedFrom", curie=UPCORE.curie('isolatedFrom'),
                   model_uri=SPARQLFUN.isolatedFrom, domain=None, range=Optional[Union[dict, Tissue]])

slots.component = Slot(uri=UPCORE.component, name="component", curie=UPCORE.curie('component'),
                   model_uri=SPARQLFUN.component, domain=None, range=Optional[Union[str, PartId]])

slots.annotation = Slot(uri=UPCORE.annotation, name="annotation", curie=UPCORE.curie('annotation'),
                   model_uri=SPARQLFUN.annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.commonTaxon = Slot(uri=UPCORE.commonTaxon, name="commonTaxon", curie=UPCORE.curie('commonTaxon'),
                   model_uri=SPARQLFUN.commonTaxon, domain=None, range=Optional[Union[str, TaxonId]])

slots.encodedBy = Slot(uri=UPCORE.encodedBy, name="encodedBy", curie=UPCORE.curie('encodedBy'),
                   model_uri=SPARQLFUN.encodedBy, domain=None, range=Optional[Union[str, GeneId]])

slots.disease = Slot(uri=UPCORE.disease, name="disease", curie=UPCORE.curie('disease'),
                   model_uri=SPARQLFUN.disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.sequence = Slot(uri=UPCORE.sequence, name="sequence", curie=UPCORE.curie('sequence'),
                   model_uri=SPARQLFUN.sequence, domain=None, range=Optional[Union[dict, Sequence]])

slots.part = Slot(uri=UPCORE.part, name="part", curie=UPCORE.curie('part'),
                   model_uri=SPARQLFUN.part, domain=None, range=Optional[Union[str, PartId]])

slots.submittedName = Slot(uri=UPCORE.submittedName, name="submittedName", curie=UPCORE.curie('submittedName'),
                   model_uri=SPARQLFUN.submittedName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.redundantTo = Slot(uri=UPCORE.redundantTo, name="redundantTo", curie=UPCORE.curie('redundantTo'),
                   model_uri=SPARQLFUN.redundantTo, domain=None, range=Optional[Union[dict, Proteome]])

slots.locatedOn = Slot(uri=UPCORE.locatedOn, name="locatedOn", curie=UPCORE.curie('locatedOn'),
                   model_uri=SPARQLFUN.locatedOn, domain=None, range=Optional[Union[dict, Molecule]])

slots.recommendedName = Slot(uri=UPCORE.recommendedName, name="recommendedName", curie=UPCORE.curie('recommendedName'),
                   model_uri=SPARQLFUN.recommendedName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.cellularComponent = Slot(uri=UPCORE.cellularComponent, name="cellularComponent", curie=UPCORE.curie('cellularComponent'),
                   model_uri=SPARQLFUN.cellularComponent, domain=None, range=Optional[Union[str, CellularComponentId]])

slots.memberOf = Slot(uri=UPCORE.memberOf, name="memberOf", curie=UPCORE.curie('memberOf'),
                   model_uri=SPARQLFUN.memberOf, domain=None, range=Optional[Union[str, ClusterId]])

slots.panproteome = Slot(uri=UPCORE.panproteome, name="panproteome", curie=UPCORE.curie('panproteome'),
                   model_uri=SPARQLFUN.panproteome, domain=None, range=Optional[Union[dict, Proteome]])

slots.nucleotideSequenceMappingIssue = Slot(uri=UPCORE.nucleotideSequenceMappingIssue, name="nucleotideSequenceMappingIssue", curie=UPCORE.curie('nucleotideSequenceMappingIssue'),
                   model_uri=SPARQLFUN.nucleotideSequenceMappingIssue, domain=None, range=Optional[Union[dict, NucleotideResource]])

slots.method = Slot(uri=UPCORE.method, name="method", curie=UPCORE.curie('method'),
                   model_uri=SPARQLFUN.method, domain=None, range=Optional[Union[dict, Method]])

slots.datatypeProperty = Slot(uri=UPCORE.datatypeProperty, name="datatypeProperty", curie=UPCORE.curie('datatypeProperty'),
                   model_uri=SPARQLFUN.datatypeProperty, domain=None, range=Optional[Union[str, NodeId]])

slots.title = Slot(uri=UPCORE.title, name="title", curie=UPCORE.curie('title'),
                   model_uri=SPARQLFUN.title, domain=None, range=Optional[str])

slots.height = Slot(uri=UPCORE.height, name="height", curie=UPCORE.curie('height'),
                   model_uri=SPARQLFUN.height, domain=None, range=Optional[int])

slots.cofactorLabel = Slot(uri=UPCORE.cofactorLabel, name="cofactorLabel", curie=UPCORE.curie('cofactorLabel'),
                   model_uri=SPARQLFUN.cofactorLabel, domain=None, range=Optional[str])

slots.precursor = Slot(uri=UPCORE.precursor, name="precursor", curie=UPCORE.curie('precursor'),
                   model_uri=SPARQLFUN.precursor, domain=None, range=Optional[Union[bool, Bool]])

slots.created = Slot(uri=UPCORE.created, name="created", curie=UPCORE.curie('created'),
                   model_uri=SPARQLFUN.created, domain=None, range=Optional[Union[str, XSDDate]])

slots.linkIsExplicit = Slot(uri=UPCORE.linkIsExplicit, name="linkIsExplicit", curie=UPCORE.curie('linkIsExplicit'),
                   model_uri=SPARQLFUN.linkIsExplicit, domain=None, range=Optional[Union[bool, Bool]])

slots.length = Slot(uri=UPCORE.length, name="length", curie=UPCORE.curie('length'),
                   model_uri=SPARQLFUN.length, domain=None, range=Optional[int])

slots.partOfLineage = Slot(uri=UPCORE.partOfLineage, name="partOfLineage", curie=UPCORE.curie('partOfLineage'),
                   model_uri=SPARQLFUN.partOfLineage, domain=None, range=Optional[Union[bool, Bool]])

slots.measuredActivity = Slot(uri=UPCORE.measuredActivity, name="measuredActivity", curie=UPCORE.curie('measuredActivity'),
                   model_uri=SPARQLFUN.measuredActivity, domain=None, range=Optional[str])

slots.curated = Slot(uri=UPCORE.curated, name="curated", curie=UPCORE.curie('curated'),
                   model_uri=SPARQLFUN.curated, domain=None, range=Optional[Union[bool, Bool]])

slots.otherName = Slot(uri=UPCORE.otherName, name="otherName", curie=UPCORE.curie('otherName'),
                   model_uri=SPARQLFUN.otherName, domain=None, range=Optional[str])

slots.experiments = Slot(uri=UPCORE.experiments, name="experiments", curie=UPCORE.curie('experiments'),
                   model_uri=SPARQLFUN.experiments, domain=None, range=Optional[int])

slots.reviewed = Slot(uri=UPCORE.reviewed, name="reviewed", curie=UPCORE.curie('reviewed'),
                   model_uri=SPARQLFUN.reviewed, domain=None, range=Optional[Union[bool, Bool]])

slots.modified = Slot(uri=UPCORE.modified, name="modified", curie=UPCORE.curie('modified'),
                   model_uri=SPARQLFUN.modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.institution = Slot(uri=UPCORE.institution, name="institution", curie=UPCORE.curie('institution'),
                   model_uri=SPARQLFUN.institution, domain=None, range=Optional[str])

slots.authorsIncomplete = Slot(uri=UPCORE.authorsIncomplete, name="authorsIncomplete", curie=UPCORE.curie('authorsIncomplete'),
                   model_uri=SPARQLFUN.authorsIncomplete, domain=None, range=Optional[Union[bool, Bool]])

slots.abstract = Slot(uri=UPCORE.abstract, name="abstract", curie=UPCORE.curie('abstract'),
                   model_uri=SPARQLFUN.abstract, domain=None, range=Optional[Union[bool, Bool]])

slots.groupcore = Slot(uri=UPCORE.group, name="groupcore", curie=UPCORE.curie('group'),
                   model_uri=SPARQLFUN.groupcore, domain=None, range=Optional[str])

slots.orfName = Slot(uri=UPCORE.orfName, name="orfName", curie=UPCORE.curie('orfName'),
                   model_uri=SPARQLFUN.orfName, domain=None, range=Optional[str])

slots.width = Slot(uri=UPCORE.width, name="width", curie=UPCORE.curie('width'),
                   model_uri=SPARQLFUN.width, domain=None, range=Optional[int])

slots.place = Slot(uri=UPCORE.place, name="place", curie=UPCORE.curie('place'),
                   model_uri=SPARQLFUN.place, domain=None, range=Optional[str])

slots.name = Slot(uri=UPCORE.name, name="name", curie=UPCORE.curie('name'),
                   model_uri=SPARQLFUN.name, domain=None, range=Optional[str])

slots.md5Checksum = Slot(uri=UPCORE.md5Checksum, name="md5Checksum", curie=UPCORE.curie('md5Checksum'),
                   model_uri=SPARQLFUN.md5Checksum, domain=None, range=Optional[str])

slots.mnemonic = Slot(uri=UPCORE.mnemonic, name="mnemonic", curie=UPCORE.curie('mnemonic'),
                   model_uri=SPARQLFUN.mnemonic, domain=None, range=Optional[str])

slots.frameshift = Slot(uri=UPCORE.frameshift, name="frameshift", curie=UPCORE.curie('frameshift'),
                   model_uri=SPARQLFUN.frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.oldMnemonic = Slot(uri=UPCORE.oldMnemonic, name="oldMnemonic", curie=UPCORE.curie('oldMnemonic'),
                   model_uri=SPARQLFUN.oldMnemonic, domain=None, range=Optional[str])

slots.chain = Slot(uri=UPCORE.chain, name="chain", curie=UPCORE.curie('chain'),
                   model_uri=SPARQLFUN.chain, domain=None, range=Optional[str])

slots.pages = Slot(uri=UPCORE.pages, name="pages", curie=UPCORE.curie('pages'),
                   model_uri=SPARQLFUN.pages, domain=None, range=Optional[str])

slots.pattern = Slot(uri=UPCORE.pattern, name="pattern", curie=UPCORE.curie('pattern'),
                   model_uri=SPARQLFUN.pattern, domain=None, range=Optional[str])

slots.substitution = Slot(uri=UPCORE.substitution, name="substitution", curie=UPCORE.curie('substitution'),
                   model_uri=SPARQLFUN.substitution, domain=None, range=Optional[str])

slots.version = Slot(uri=UPCORE.version, name="version", curie=UPCORE.curie('version'),
                   model_uri=SPARQLFUN.version, domain=None, range=Optional[int])

slots.implicit = Slot(uri=UPCORE.implicit, name="implicit", curie=UPCORE.curie('implicit'),
                   model_uri=SPARQLFUN.implicit, domain=None, range=Optional[Union[bool, Bool]])

slots.measuredAffinity = Slot(uri=UPCORE.measuredAffinity, name="measuredAffinity", curie=UPCORE.curie('measuredAffinity'),
                   model_uri=SPARQLFUN.measuredAffinity, domain=None, range=Optional[str])

slots.obsolete = Slot(uri=UPCORE.obsolete, name="obsolete", curie=UPCORE.curie('obsolete'),
                   model_uri=SPARQLFUN.obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.locator = Slot(uri=UPCORE.locator, name="locator", curie=UPCORE.curie('locator'),
                   model_uri=SPARQLFUN.locator, domain=None, range=Optional[str])

slots.mass = Slot(uri=UPCORE.mass, name="mass", curie=UPCORE.curie('mass'),
                   model_uri=SPARQLFUN.mass, domain=None, range=Optional[int])

slots.uriTemplate = Slot(uri=UPCORE.uriTemplate, name="uriTemplate", curie=UPCORE.curie('uriTemplate'),
                   model_uri=SPARQLFUN.uriTemplate, domain=None, range=Optional[str])

slots.scientificName = Slot(uri=UPCORE.scientificName, name="scientificName", curie=UPCORE.curie('scientificName'),
                   model_uri=SPARQLFUN.scientificName, domain=None, range=Optional[str])

slots.alias = Slot(uri=UPCORE.alias, name="alias", curie=UPCORE.curie('alias'),
                   model_uri=SPARQLFUN.alias, domain=None, range=Optional[str])

slots.exclusionReason = Slot(uri=UPCORE.exclusionReason, name="exclusionReason", curie=UPCORE.curie('exclusionReason'),
                   model_uri=SPARQLFUN.exclusionReason, domain=None, range=Optional[str])

slots.measuredError = Slot(uri=UPCORE.measuredError, name="measuredError", curie=UPCORE.curie('measuredError'),
                   model_uri=SPARQLFUN.measuredError, domain=None, range=Optional[float])

slots.publisher = Slot(uri=UPCORE.publisher, name="publisher", curie=UPCORE.curie('publisher'),
                   model_uri=SPARQLFUN.publisher, domain=None, range=Optional[str])

slots.maximum = Slot(uri=UPCORE.maximum, name="maximum", curie=UPCORE.curie('maximum'),
                   model_uri=SPARQLFUN.maximum, domain=None, range=Optional[float])

slots.structuredNameType = Slot(uri=UPCORE.structuredNameType, name="structuredNameType", curie=UPCORE.curie('structuredNameType'),
                   model_uri=SPARQLFUN.structuredNameType, domain=None, range=Optional[str])

slots.editor = Slot(uri=UPCORE.editor, name="editor", curie=UPCORE.curie('editor'),
                   model_uri=SPARQLFUN.editor, domain=None, range=Optional[str])

slots.author = Slot(uri=UPCORE.author, name="author", curie=UPCORE.curie('author'),
                   model_uri=SPARQLFUN.author, domain=None, range=Optional[str])

slots.measuredValue = Slot(uri=UPCORE.measuredValue, name="measuredValue", curie=UPCORE.curie('measuredValue'),
                   model_uri=SPARQLFUN.measuredValue, domain=None, range=Optional[float])

slots.negative = Slot(uri=UPCORE.negative, name="negative", curie=UPCORE.curie('negative'),
                   model_uri=SPARQLFUN.negative, domain=None, range=Optional[Union[bool, Bool]])

slots.shortCoden = Slot(uri=UPCORE.shortCoden, name="shortCoden", curie=UPCORE.curie('shortCoden'),
                   model_uri=SPARQLFUN.shortCoden, domain=None, range=Optional[str])

slots.xeno = Slot(uri=UPCORE.xeno, name="xeno", curie=UPCORE.curie('xeno'),
                   model_uri=SPARQLFUN.xeno, domain=None, range=Optional[Union[bool, Bool]])

slots.synonym = Slot(uri=UPCORE.synonym, name="synonym", curie=UPCORE.curie('synonym'),
                   model_uri=SPARQLFUN.synonym, domain=None, range=Optional[str])

slots.scope = Slot(uri=UPCORE.scope, name="scope", curie=UPCORE.curie('scope'),
                   model_uri=SPARQLFUN.scope, domain=None, range=Optional[str])

slots.urlTemplate = Slot(uri=UPCORE.urlTemplate, name="urlTemplate", curie=UPCORE.curie('urlTemplate'),
                   model_uri=SPARQLFUN.urlTemplate, domain=None, range=Optional[str])

slots.resolution = Slot(uri=UPCORE.resolution, name="resolution", curie=UPCORE.curie('resolution'),
                   model_uri=SPARQLFUN.resolution, domain=None, range=Optional[float])

slots.manual = Slot(uri=UPCORE.manual, name="manual", curie=UPCORE.curie('manual'),
                   model_uri=SPARQLFUN.manual, domain=None, range=Optional[Union[bool, Bool]])

slots.certain = Slot(uri=UPCORE.certain, name="certain", curie=UPCORE.curie('certain'),
                   model_uri=SPARQLFUN.certain, domain=None, range=Optional[Union[bool, Bool]])

slots.complete = Slot(uri=UPCORE.complete, name="complete", curie=UPCORE.curie('complete'),
                   model_uri=SPARQLFUN.complete, domain=None, range=Optional[Union[bool, Bool]])

slots.nestedTriple__xobject = Slot(uri=RDF.xobject, name="nestedTriple__xobject", curie=RDF.curie('xobject'),
                   model_uri=SPARQLFUN.nestedTriple__xobject, domain=None, range=Optional[Union[str, NodeId]])

slots.basicClass__subClassOf = Slot(uri=RDFS.subClassOf, name="basicClass__subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=SPARQLFUN.basicClass__subClassOf, domain=None, range=Optional[Union[Union[str, ClassNodeId], List[Union[str, ClassNodeId]]]])

slots.statement_node_statements = Slot(uri=SPARQLFUN.node_statements, name="statement_node_statements", curie=SPARQLFUN.curie('node_statements'),
                   model_uri=SPARQLFUN.statement_node_statements, domain=Statement, range=Optional[Union[Union[dict, "NodeToNodeStatement"], List[Union[dict, "NodeToNodeStatement"]]]])

slots.statement_value_statements = Slot(uri=SPARQLFUN.value_statements, name="statement_value_statements", curie=SPARQLFUN.curie('value_statements'),
                   model_uri=SPARQLFUN.statement_value_statements, domain=Statement, range=Optional[Union[Union[dict, "NodeToValueStatement"], List[Union[dict, "NodeToValueStatement"]]]])

slots.node_to_node_triple_object = Slot(uri=RDF.object, name="node to node triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_node_triple_object, domain=NodeToNodeTriple, range=Optional[Union[str, NodeId]])

slots.node_to_node_statement_object = Slot(uri=RDF.object, name="node to node statement_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_node_statement_object, domain=NodeToNodeStatement, range=Optional[Union[str, NodeId]])

slots.node_to_value_triple_object = Slot(uri=RDF.object, name="node to value triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_value_triple_object, domain=NodeToValueTriple, range=Optional[str])

slots.node_to_value_statement_object = Slot(uri=RDF.object, name="node to value statement_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_value_statement_object, domain=NodeToValueStatement, range=Optional[str])

slots.rdf_type_triple_object = Slot(uri=RDF.object, name="rdf type triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.rdf_type_triple_object, domain=RdfTypeTriple, range=Optional[Union[str, ClassNodeId]])

slots.rdf_type_statement_object = Slot(uri=RDF.object, name="rdf type statement_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.rdf_type_statement_object, domain=RdfTypeStatement, range=Optional[Union[str, ClassNodeId]])

slots.rdfs_subclass_of_triple_subject = Slot(uri=RDF.subject, name="rdfs subclass of triple_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.rdfs_subclass_of_triple_subject, domain=RdfsSubclassOfTriple, range=Optional[Union[str, ClassNodeId]])

slots.rdfs_subclass_of_triple_object = Slot(uri=RDF.object, name="rdfs subclass of triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.rdfs_subclass_of_triple_object, domain=RdfsSubclassOfTriple, range=Optional[Union[str, ClassNodeId]])

slots.rdfs_subproperty_of_triple_subject = Slot(uri=RDF.subject, name="rdfs subproperty of triple_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.rdfs_subproperty_of_triple_subject, domain=RdfsSubpropertyOfTriple, range=Optional[Union[str, PropertyNodeId]])

slots.rdfs_subproperty_of_triple_object = Slot(uri=RDF.object, name="rdfs subproperty of triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.rdfs_subproperty_of_triple_object, domain=RdfsSubpropertyOfTriple, range=Optional[Union[str, PropertyNodeId]])

slots.rdfs_label_triple_value = Slot(uri=SPARQLFUN_RDF.value, name="rdfs label triple_value", curie=SPARQLFUN_RDF.curie('value'),
                   model_uri=SPARQLFUN.rdfs_label_triple_value, domain=RdfsLabelTriple, range=Optional[str])

slots.iri_node_id = Slot(uri=SPARQLFUN_RDF.id, name="iri node_id", curie=SPARQLFUN_RDF.curie('id'),
                   model_uri=SPARQLFUN.iri_node_id, domain=IriNode, range=Union[str, IriNodeId],
                   pattern=re.compile(r'^_:'))

slots.nested_triple_subject = Slot(uri=RDF.subject, name="nested triple_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.nested_triple_subject, domain=NestedTriple, range=Optional[Union[str, NodeId]])

slots.nested_triple_object = Slot(uri=RDF.object, name="nested triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.nested_triple_object, domain=NestedTriple, range=Optional[Union[str, NodeId]])

slots.equivalence_triple_mixin_subject = Slot(uri=RDF.subject, name="equivalence triple mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.equivalence_triple_mixin_subject, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.equivalence_triple_mixin_object = Slot(uri=RDF.object, name="equivalence triple mixin_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.equivalence_triple_mixin_object, domain=None, range=Optional[Union[str, ClassNodeId]])

slots.owl_named_equivalent_class_triple_subject = Slot(uri=RDF.subject, name="owl named equivalent class triple_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.owl_named_equivalent_class_triple_subject, domain=OwlNamedEquivalentClassTriple, range=Optional[Union[str, ClassNodeId]])

slots.owl_named_equivalent_class_triple_object = Slot(uri=RDF.object, name="owl named equivalent class triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.owl_named_equivalent_class_triple_object, domain=OwlNamedEquivalentClassTriple, range=Optional[Union[str, ClassNodeId]])

slots.describe_equivalent_expression_results = Slot(uri=RESULTSET.results, name="describe equivalent expression_results", curie=RESULTSET.curie('results'),
                   model_uri=SPARQLFUN.describe_equivalent_expression_results, domain=DescribeEquivalentExpression, range=Optional[Union[Union[str, ClassNodeId], List[Union[str, ClassNodeId]]]])

slots.relation_graph_quad_graph = Slot(uri=RDFS.isDefinedBy, name="relation graph quad_graph", curie=RDFS.curie('isDefinedBy'),
                   model_uri=SPARQLFUN.relation_graph_quad_graph, domain=RelationGraphQuad, range=Optional[Union[str, NodeId]])

slots.non_redundant_quad_graph = Slot(uri=RDFS.isDefinedBy, name="non redundant quad_graph", curie=RDFS.curie('isDefinedBy'),
                   model_uri=SPARQLFUN.non_redundant_quad_graph, domain=NonRedundantQuad, range=Optional[Union[str, ClassNodeId]])

slots.taxon_applicable_subject = Slot(uri=RDF.subject, name="taxon applicable_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.taxon_applicable_subject, domain=None, range=Optional[Union[str, TaxonApplicableClassId]])

slots.taxon_applicable_object = Slot(uri=RDF.object, name="taxon applicable_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.taxon_applicable_object, domain=None, range=Optional[Union[str, TaxonClassId]])

slots.obo_class_query_results = Slot(uri=RESULTSET.results, name="obo class query_results", curie=RESULTSET.curie('results'),
                   model_uri=SPARQLFUN.obo_class_query_results, domain=OboClassQuery, range=Optional[Union[Union[str, OboClassId], List[Union[str, OboClassId]]]])

slots.deprecated_obo_class_query_results = Slot(uri=RESULTSET.results, name="deprecated obo class query_results", curie=RESULTSET.curie('results'),
                   model_uri=SPARQLFUN.deprecated_obo_class_query_results, domain=DeprecatedOboClassQuery, range=Optional[Union[Union[str, OboClassId], List[Union[str, OboClassId]]]])

slots.class_taxon_exclusion_via_never_in_subject = Slot(uri=RDF.subject, name="class taxon exclusion via never in_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_via_never_in_subject, domain=ClassTaxonExclusionViaNeverIn, range=Optional[Union[str, NodeId]])

slots.class_taxon_exclusion_via_never_in_object = Slot(uri=RDF.object, name="class taxon exclusion via never in_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_via_never_in_object, domain=ClassTaxonExclusionViaNeverIn, range=Optional[Union[dict, NodeOrLiteral]])

slots.class_taxon_exclusion_via_only_in_subject = Slot(uri=RDF.subject, name="class taxon exclusion via only in_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_via_only_in_subject, domain=ClassTaxonExclusionViaOnlyIn, range=Optional[Union[str, NodeId]])

slots.class_taxon_exclusion_via_only_in_object = Slot(uri=RDF.object, name="class taxon exclusion via only in_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_via_only_in_object, domain=ClassTaxonExclusionViaOnlyIn, range=Optional[Union[dict, NodeOrLiteral]])

slots.class_taxon_exclusion_subject = Slot(uri=RDF.subject, name="class taxon exclusion_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_subject, domain=ClassTaxonExclusion, range=Optional[Union[str, NodeId]])

slots.class_taxon_exclusion_object = Slot(uri=RDF.object, name="class taxon exclusion_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.class_taxon_exclusion_object, domain=ClassTaxonExclusion, range=Optional[Union[dict, NodeOrLiteral]])

slots.blood_vessel_subcategory = Slot(uri=SPARQLFUN.subcategory, name="blood vessel_subcategory", curie=SPARQLFUN.curie('subcategory'),
                   model_uri=SPARQLFUN.blood_vessel_subcategory, domain=BloodVessel, range=Optional[Union[str, "BloodVesselSubcategory"]])

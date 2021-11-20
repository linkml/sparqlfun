# Auto generated from sparqlfun.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-19T17:44:46
# Schema: sparqlfun
#
# id: https://w3id.org/sparqlfun
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
from linkml_runtime.linkml_model.types import Ncname, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import NCName, URI, URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SPARQLFUN = CurieNamespace('sparqlfun', 'https://w3id.org/sparqlfun/')
SPARQLFUN_OMO = CurieNamespace('sparqlfun_omo', 'https://w3id.org/sparqlfun/omo')
SPARQLFUN_RDF = CurieNamespace('sparqlfun_rdf', 'https://w3id.org/sparqlfun/rdf')
SPARQLFUN_UBERGRAPH = CurieNamespace('sparqlfun_ubergraph', 'https://w3id.org/sparqlfun/ubergraph')
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


class BasicClassId(NodeId):
    pass


class TaxonApplicableClassId(ClassNodeId):
    pass


class TaxonClassId(ClassNodeId):
    pass


class OboClassId(ClassNodeId):
    pass


class OboClassFilteredId(ClassNodeId):
    pass


class GenericResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN.GenericResult
    class_class_curie: ClassVar[str] = "sparqlfun:GenericResult"
    class_name: ClassVar[str] = "GenericResult"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.GenericResult


@dataclass
class ResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN.ResultSet
    class_class_curie: ClassVar[str] = "sparqlfun:ResultSet"
    class_name: ClassVar[str] = "ResultSet"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.ResultSet

    results: Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, GenericResult) else GenericResult(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)


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
    Represents an RDF triple
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Triple

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class Quad(Triple):
    """
    Represents an RDF triple plus named graph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_RDF.Quad
    class_class_curie: ClassVar[str] = "sparqlfun_rdf:Quad"
    class_name: ClassVar[str] = "quad"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.Quad

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, PropertyNodeId]] = None
    object: Optional[str] = None
    graph: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PropertyNodeId):
            self.predicate = PropertyNodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        if self.graph is not None and not isinstance(self.graph, NodeId):
            self.graph = NodeId(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class NodeToNodeTriple(Triple):
    """
    A triple where object is a node
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


class DefinitionTriple(NodeToValueTriple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_OMO.DefinitionTriple
    class_class_curie: ClassVar[str] = "sparqlfun_omo:DefinitionTriple"
    class_name: ClassVar[str] = "definition triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.DefinitionTriple


@dataclass
class OboClass(ClassNode):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "obo class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.OboClass

    id: Union[str, OboClassId] = None
    definition: Optional[str] = None
    exact_synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OboClassId):
            self.id = OboClassId(self.id)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        super().__post_init__(**kwargs)


class UbergraphTaxonClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.UbergraphTaxonClass
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:UbergraphTaxonClass"
    class_name: ClassVar[str] = "ubergraph taxon class"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.UbergraphTaxonClass


class UbergraphQuad(RelationGraphQuad):
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


class InTaxonTriple(Triple):
    """
    In ubergraph, an in-taxon triple is pre-inferred
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.InTaxonTriple
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:InTaxonTriple"
    class_name: ClassVar[str] = "in taxon triple"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.InTaxonTriple


@dataclass
class InferredNeverInTaxon(Triple):
    """
    We infer via join
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.InferredNeverInTaxon
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:InferredNeverInTaxon"
    class_name: ClassVar[str] = "inferred never in taxon"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.InferredNeverInTaxon

    subject_predicate: Optional[str] = None
    class_with_constraint: Optional[str] = None
    direct_taxon: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_predicate is not None and not isinstance(self.subject_predicate, str):
            self.subject_predicate = str(self.subject_predicate)

        if self.class_with_constraint is not None and not isinstance(self.class_with_constraint, str):
            self.class_with_constraint = str(self.class_with_constraint)

        if self.direct_taxon is not None and not isinstance(self.direct_taxon, str):
            self.direct_taxon = str(self.direct_taxon)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseCommonAncestor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonAncestor"
    class_name: ClassVar[str] = "pairwise common ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonAncestor

    node1: Optional[str] = None
    node2: Optional[str] = None
    predicate1: Optional[Union[str, PropertyNodeId]] = None
    predicate2: Optional[Union[str, PropertyNodeId]] = None
    ancestor: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.node1 is not None and not isinstance(self.node1, str):
            self.node1 = str(self.node1)

        if self.node2 is not None and not isinstance(self.node2, str):
            self.node2 = str(self.node2)

        if self.predicate1 is not None and not isinstance(self.predicate1, PropertyNodeId):
            self.predicate1 = PropertyNodeId(self.predicate1)

        if self.predicate2 is not None and not isinstance(self.predicate2, PropertyNodeId):
            self.predicate2 = PropertyNodeId(self.predicate2)

        if self.ancestor is not None and not isinstance(self.ancestor, str):
            self.ancestor = str(self.ancestor)

        super().__post_init__(**kwargs)


class PairwiseCommonSubClassAncestor(PairwiseCommonAncestor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPARQLFUN_UBERGRAPH.PairwiseCommonSubClassAncestor
    class_class_curie: ClassVar[str] = "sparqlfun_ubergraph:PairwiseCommonSubClassAncestor"
    class_name: ClassVar[str] = "pairwise common SubClass ancestor"
    class_model_uri: ClassVar[URIRef] = SPARQLFUN.PairwiseCommonSubClassAncestor


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


# Enumerations
class UberGraphSourceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="UberGraphSourceEnum",
    )

# Slots
class slots:
    pass

slots.results = Slot(uri=SPARQLFUN.results, name="results", curie=SPARQLFUN.curie('results'),
                   model_uri=SPARQLFUN.results, domain=None, range=Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]])

slots.id = Slot(uri=SPARQLFUN_RDF.id, name="id", curie=SPARQLFUN_RDF.curie('id'),
                   model_uri=SPARQLFUN.id, domain=None, range=URIRef)

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.subject, domain=None, range=Optional[Union[str, NodeId]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=SPARQLFUN.predicate, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.object, domain=None, range=Optional[str])

slots.graph = Slot(uri=SPARQLFUN_RDF.graph, name="graph", curie=SPARQLFUN_RDF.curie('graph'),
                   model_uri=SPARQLFUN.graph, domain=None, range=Optional[Union[str, NodeId]])

slots.type = Slot(uri=SPARQLFUN_RDF.type, name="type", curie=SPARQLFUN_RDF.curie('type'),
                   model_uri=SPARQLFUN.type, domain=None, range=Optional[Union[str, NodeId]])

slots.datatype = Slot(uri=SPARQLFUN_RDF.datatype, name="datatype", curie=SPARQLFUN_RDF.curie('datatype'),
                   model_uri=SPARQLFUN.datatype, domain=None, range=Optional[str])

slots.value = Slot(uri=SPARQLFUN_RDF.value, name="value", curie=SPARQLFUN_RDF.curie('value'),
                   model_uri=SPARQLFUN.value, domain=None, range=Optional[Union[str, LiteralAsStringType]])

slots.language = Slot(uri=SPARQLFUN_RDF.language, name="language", curie=SPARQLFUN_RDF.curie('language'),
                   model_uri=SPARQLFUN.language, domain=None, range=Optional[str])

slots.prefix = Slot(uri=SH.prefix, name="prefix", curie=SH.curie('prefix'),
                   model_uri=SPARQLFUN.prefix, domain=None, range=Optional[Union[str, NCName]])

slots.base = Slot(uri=SH.namespace, name="base", curie=SH.curie('namespace'),
                   model_uri=SPARQLFUN.base, domain=None, range=Optional[Union[str, URI]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=SPARQLFUN.description, domain=None, range=Optional[str])

slots.definition = Slot(uri=IAO['0000115'], name="definition", curie=IAO.curie('0000115'),
                   model_uri=SPARQLFUN.definition, domain=None, range=Optional[str])

slots.exact_synonyms = Slot(uri=OBOINOWL.hasExactSynonym, name="exact_synonyms", curie=OBOINOWL.curie('hasExactSynonym'),
                   model_uri=SPARQLFUN.exact_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.ancestor = Slot(uri=SPARQLFUN_UBERGRAPH.ancestor, name="ancestor", curie=SPARQLFUN_UBERGRAPH.curie('ancestor'),
                   model_uri=SPARQLFUN.ancestor, domain=None, range=Optional[str])

slots.node1 = Slot(uri=SPARQLFUN_UBERGRAPH.node1, name="node1", curie=SPARQLFUN_UBERGRAPH.curie('node1'),
                   model_uri=SPARQLFUN.node1, domain=None, range=Optional[str])

slots.node2 = Slot(uri=SPARQLFUN_UBERGRAPH.node2, name="node2", curie=SPARQLFUN_UBERGRAPH.curie('node2'),
                   model_uri=SPARQLFUN.node2, domain=None, range=Optional[str])

slots.predicate1 = Slot(uri=SPARQLFUN_UBERGRAPH.predicate1, name="predicate1", curie=SPARQLFUN_UBERGRAPH.curie('predicate1'),
                   model_uri=SPARQLFUN.predicate1, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.predicate2 = Slot(uri=SPARQLFUN_UBERGRAPH.predicate2, name="predicate2", curie=SPARQLFUN_UBERGRAPH.curie('predicate2'),
                   model_uri=SPARQLFUN.predicate2, domain=None, range=Optional[Union[str, PropertyNodeId]])

slots.subject_predicate = Slot(uri=SPARQLFUN_UBERGRAPH.subject_predicate, name="subject_predicate", curie=SPARQLFUN_UBERGRAPH.curie('subject_predicate'),
                   model_uri=SPARQLFUN.subject_predicate, domain=None, range=Optional[str])

slots.class_with_constraint = Slot(uri=SPARQLFUN_UBERGRAPH.class_with_constraint, name="class_with_constraint", curie=SPARQLFUN_UBERGRAPH.curie('class_with_constraint'),
                   model_uri=SPARQLFUN.class_with_constraint, domain=None, range=Optional[str])

slots.direct_taxon = Slot(uri=SPARQLFUN_UBERGRAPH.direct_taxon, name="direct_taxon", curie=SPARQLFUN_UBERGRAPH.curie('direct_taxon'),
                   model_uri=SPARQLFUN.direct_taxon, domain=None, range=Optional[str])

slots.query_has_subclass_ancestor = Slot(uri=SPARQLFUN_UBERGRAPH.query_has_subclass_ancestor, name="query_has_subclass_ancestor", curie=SPARQLFUN_UBERGRAPH.curie('query_has_subclass_ancestor'),
                   model_uri=SPARQLFUN.query_has_subclass_ancestor, domain=None, range=Optional[str])

slots.basicClass__subClassOf = Slot(uri=RDFS.subClassOf, name="basicClass__subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=SPARQLFUN.basicClass__subClassOf, domain=None, range=Optional[Union[Union[str, ClassNodeId], List[Union[str, ClassNodeId]]]])

slots.node_to_node_triple_object = Slot(uri=RDF.object, name="node to node triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_node_triple_object, domain=NodeToNodeTriple, range=Optional[Union[str, NodeId]])

slots.node_to_value_triple_object = Slot(uri=RDF.object, name="node to value triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.node_to_value_triple_object, domain=NodeToValueTriple, range=Optional[str])

slots.rdf_type_triple_object = Slot(uri=RDF.object, name="rdf type triple_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.rdf_type_triple_object, domain=RdfTypeTriple, range=Optional[Union[str, ClassNodeId]])

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

slots.relation_graph_quad_graph = Slot(uri=SPARQLFUN_RDF.graph, name="relation graph quad_graph", curie=SPARQLFUN_RDF.curie('graph'),
                   model_uri=SPARQLFUN.relation_graph_quad_graph, domain=RelationGraphQuad, range=Optional[Union[str, NodeId]])

slots.non_redundant_quad_graph = Slot(uri=SPARQLFUN_RDF.graph, name="non redundant quad_graph", curie=SPARQLFUN_RDF.curie('graph'),
                   model_uri=SPARQLFUN.non_redundant_quad_graph, domain=NonRedundantQuad, range=Optional[Union[str, ClassNodeId]])

slots.taxon_applicable_subject = Slot(uri=RDF.subject, name="taxon applicable_subject", curie=RDF.curie('subject'),
                   model_uri=SPARQLFUN.taxon_applicable_subject, domain=None, range=Optional[Union[str, TaxonApplicableClassId]])

slots.taxon_applicable_object = Slot(uri=RDF.object, name="taxon applicable_object", curie=RDF.curie('object'),
                   model_uri=SPARQLFUN.taxon_applicable_object, domain=None, range=Optional[Union[str, TaxonClassId]])

# Auto generated from gocam_queries.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-24T13:47:29
# Schema: gocam-queries
#
# id: https://linkml.io/sparqlfun/gocam_queries
# description: Abstractions for querying gocam
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
from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
DOI = CurieNamespace('DOI', 'http://dx.doi.org/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
OBAN = CurieNamespace('OBAN', 'http://example.org/UNKNOWN/OBAN/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
GOCAM = CurieNamespace('gocam', 'https://w3id.org/gocam/')
GOCAM_QUERIES = CurieNamespace('gocam_queries', 'https://linkml.io/sparqlfun/gocam_queries')
GOMODEL = CurieNamespace('gomodel', 'http://model.geneontology.org/')
GOSHAPES = CurieNamespace('goshapes', 'http://purl.obolibrary.org/obo/go/shapes/')
LEGO = CurieNamespace('lego', 'http://geneontology.org/lego/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RESULTSET = CurieNamespace('resultset', 'https://linkml.io/sparqlfun/resultset')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GOCAM_QUERIES


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = GOCAM_QUERIES.ChemicalFormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the biolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the biolink class, for example biolink:Gene. For an RDF representation, the value should be a URI such as https://w3id.org/biolink/vocab/Gene """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = GOCAM_QUERIES.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = GOCAM_QUERIES.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = GOCAM_QUERIES.LabelType


class PredicateType(Uriorcurie):
    """ A RO identifier """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = GOCAM_QUERIES.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = GOCAM_QUERIES.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = GOCAM_QUERIES.SymbolType


# Class references
class ModelInfoId(extended_str):
    pass


class ModelElementsId(extended_str):
    pass


class ModelElementsInferredTypesId(extended_str):
    pass


class ModelInteractionsId(extended_str):
    pass


class ModelStatisticsId(extended_str):
    pass


class ModelCausalStatisticsId(extended_str):
    pass


class CausalModelId(extended_str):
    pass


class ModelIdQueryId(extended_str):
    pass


class BindingBindingKey(extended_str):
    pass


class EntityId(extended_str):
    pass


class ModelId(EntityId):
    pass


class DomainEntityId(EntityId):
    pass


class MolecularActivityId(DomainEntityId):
    pass


class BiologicalProcessId(DomainEntityId):
    pass


class AnatomicalEntityId(DomainEntityId):
    pass


class ChemicalEntityId(DomainEntityId):
    pass


class InformationBiomacromoleculeId(ChemicalEntityId):
    pass


class OntologyClassId(extended_str):
    pass


class InformationEntityId(EntityId):
    pass


class PublicationId(InformationEntityId):
    pass


class EvidenceId(InformationEntityId):
    pass


class DomainEntityMixinId(extended_str):
    pass


class ActivityOrProcessId(DomainEntityMixinId):
    pass


class ProcessOrPhaseId(DomainEntityMixinId):
    pass


class ContinuantId(DomainEntityMixinId):
    pass


@dataclass
class ModelInfo(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelInfo
    class_class_curie: ClassVar[str] = "gocam_queries:ModelInfo"
    class_name: ClassVar[str] = "model info"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelInfo

    id: Union[str, ModelInfoId] = None
    title: Optional[str] = None
    state: Optional[Union[str, "ModelStateEnum"]] = None
    provided_by: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelInfoId):
            self.id = ModelInfoId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        super().__post_init__(**kwargs)


@dataclass
class ModelElements(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelElements
    class_class_curie: ClassVar[str] = "gocam_queries:ModelElements"
    class_name: ClassVar[str] = "model elements"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelElements

    id: Union[str, ModelElementsId] = None
    object: Union[str, EntityId] = None
    title: Optional[str] = None
    subject: Optional[Union[str, DomainEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelElementsId):
            self.id = ModelElementsId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, EntityId):
            self.object = EntityId(self.object)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ModelElementsInferredTypes(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelElementsInferredTypes
    class_class_curie: ClassVar[str] = "gocam_queries:ModelElementsInferredTypes"
    class_name: ClassVar[str] = "model elements inferred types"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelElementsInferredTypes

    id: Union[str, ModelElementsInferredTypesId] = None
    object: Union[str, EntityId] = None
    type: Union[str, OntologyClassId] = None
    title: Optional[str] = None
    subject: Optional[Union[str, DomainEntityId]] = None
    graph: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelElementsInferredTypesId):
            self.id = ModelElementsInferredTypesId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, EntityId):
            self.object = EntityId(self.object)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.graph is not None and not isinstance(self.graph, str):
            self.graph = str(self.graph)

        super().__post_init__(**kwargs)


@dataclass
class ModelInteractions(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelInteractions
    class_class_curie: ClassVar[str] = "gocam_queries:ModelInteractions"
    class_name: ClassVar[str] = "model interactions"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelInteractions

    id: Union[str, ModelInteractionsId] = None
    object: Union[str, EntityId] = None
    title: Optional[str] = None
    subject: Optional[Union[str, DomainEntityId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelInteractionsId):
            self.id = ModelInteractionsId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, EntityId):
            self.object = EntityId(self.object)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ModelStatistics(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelStatistics
    class_class_curie: ClassVar[str] = "gocam_queries:ModelStatistics"
    class_name: ClassVar[str] = "model statistics"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelStatistics

    id: Union[str, ModelStatisticsId] = None
    activity_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelStatisticsId):
            self.id = ModelStatisticsId(self.id)

        if self.activity_count is not None and not isinstance(self.activity_count, int):
            self.activity_count = int(self.activity_count)

        super().__post_init__(**kwargs)


@dataclass
class ModelCausalStatistics(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelCausalStatistics
    class_class_curie: ClassVar[str] = "gocam_queries:ModelCausalStatistics"
    class_name: ClassVar[str] = "model causal statistics"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelCausalStatistics

    id: Union[str, ModelCausalStatisticsId] = None
    activity_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelCausalStatisticsId):
            self.id = ModelCausalStatisticsId(self.id)

        if self.activity_count is not None and not isinstance(self.activity_count, int):
            self.activity_count = int(self.activity_count)

        super().__post_init__(**kwargs)


@dataclass
class CausalModel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.CausalModel
    class_class_curie: ClassVar[str] = "gocam_queries:CausalModel"
    class_name: ClassVar[str] = "causal model"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.CausalModel

    id: Union[str, CausalModelId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CausalModelId):
            self.id = CausalModelId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ModelQuery(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelQuery
    class_class_curie: ClassVar[str] = "gocam_queries:ModelQuery"
    class_name: ClassVar[str] = "model query"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelQuery

    results: Optional[Union[Union[str, ModelId], List[Union[str, ModelId]]]] = empty_list()
    state: Optional[Union[str, "ModelStateEnum"]] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    title_regex: Optional[str] = None
    provided_by: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, ModelId) else ModelId(v) for v in self.results]

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.title_regex is not None and not isinstance(self.title_regex, str):
            self.title_regex = str(self.title_regex)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        super().__post_init__(**kwargs)


@dataclass
class ModelIdQuery(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelIdQuery
    class_class_curie: ClassVar[str] = "gocam_queries:ModelIdQuery"
    class_name: ClassVar[str] = "model id query"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelIdQuery

    id: Union[str, ModelIdQueryId] = None
    title: Optional[str] = None
    state: Optional[Union[str, "ModelStateEnum"]] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    title_regex: Optional[str] = None
    provided_by: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelIdQueryId):
            self.id = ModelIdQueryId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.title_regex is not None and not isinstance(self.title_regex, str):
            self.title_regex = str(self.title_regex)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        super().__post_init__(**kwargs)


@dataclass
class ModelQueryTODO(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelQueryTODO
    class_class_curie: ClassVar[str] = "gocam_queries:ModelQueryTODO"
    class_name: ClassVar[str] = "model query TODO"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ModelQueryTODO

    results: Optional[Union[Union[dict, "GenericResult"], List[Union[dict, "GenericResult"]]]] = empty_list()
    state: Optional[Union[str, "ModelStateEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, GenericResult) else GenericResult(**as_dict(v)) for v in self.results]

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        super().__post_init__(**kwargs)


class GenericResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.GenericResult
    class_class_curie: ClassVar[str] = "resultset:GenericResult"
    class_name: ClassVar[str] = "GenericResult"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.GenericResult


@dataclass
class ResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.ResultSet
    class_class_curie: ClassVar[str] = "resultset:ResultSet"
    class_name: ClassVar[str] = "ResultSet"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ResultSet

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
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Binding

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


@dataclass
class Entity(YAMLRoot):
    """
    Abstract base class for any biological entity or activity or process in a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Entity
    class_class_curie: ClassVar[str] = "gocam:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Entity

    id: Union[str, EntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Model(Entity):
    """
    A collection of GO-CAM entities and associated metadata. A model combines multiple simple GO annotations into an
    integrated, semantically precise and computable model of biological function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Model
    class_class_curie: ClassVar[str] = "gocam:Model"
    class_name: ClassVar[str] = "model"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Model

    id: Union[str, ModelId] = None
    title: Optional[str] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    state: Optional[Union[str, "ModelStateEnum"]] = None
    provided_by: Optional[str] = None
    molecular_activity_set: Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, "MolecularActivity"]], List[Union[dict, "MolecularActivity"]]]] = empty_dict()
    biological_process_set: Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, "BiologicalProcess"]], List[Union[dict, "BiologicalProcess"]]]] = empty_dict()
    information_biomacromolecule_set: Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, "InformationBiomacromolecule"]], List[Union[dict, "InformationBiomacromolecule"]]]] = empty_dict()
    chemical_entity_set: Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], List[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    ontology_class_set: Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, "OntologyClass"]], List[Union[dict, "OntologyClass"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        self._normalize_inlined_as_dict(slot_name="molecular_activity_set", slot_type=MolecularActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="biological_process_set", slot_type=BiologicalProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="information_biomacromolecule_set", slot_type=InformationBiomacromolecule, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="chemical_entity_set", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="ontology_class_set", slot_type=OntologyClass, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DomainEntity(Entity):
    """
    Abstract entity for representing any part of a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainEntity
    class_class_curie: ClassVar[str] = "gocam:DomainEntity"
    class_name: ClassVar[str] = "domain entity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.DomainEntity

    id: Union[str, DomainEntityId] = None
    type: Union[str, OntologyClassId] = None
    type_inferences: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainEntityId):
            self.id = DomainEntityId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if not isinstance(self.type_inferences, list):
            self.type_inferences = [self.type_inferences] if self.type_inferences is not None else []
        self.type_inferences = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.type_inferences]

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(DomainEntity):
    """
    An instance of a GO molecular function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MolecularActivity
    class_class_curie: ClassVar[str] = "gocam:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    type: Union[str, OntologyClassId] = None
    has_activity_causal_associations: Optional[Union[Union[dict, "ActivityToActivityCausalAssociation"], List[Union[dict, "ActivityToActivityCausalAssociation"]]]] = empty_list()
    has_process_causal_associations: Optional[Union[Union[dict, "ActivityToProcessCausalAssociation"], List[Union[dict, "ActivityToProcessCausalAssociation"]]]] = empty_list()
    happens_during: Optional[Union[Union[dict, "HappensDuringAssociation"], List[Union[dict, "HappensDuringAssociation"]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ProcessPartOfAssociation"], List[Union[dict, "ProcessPartOfAssociation"]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "EnabledByAssociation"], List[Union[dict, "EnabledByAssociation"]]]] = empty_list()
    has_input: Optional[Union[Union[dict, "HasInputAssociation"], List[Union[dict, "HasInputAssociation"]]]] = empty_list()
    occurs_in: Optional[Union[Union[dict, "OccursInAssociation"], List[Union[dict, "OccursInAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        self._normalize_inlined_as_list(slot_name="has_activity_causal_associations", slot_type=ActivityToActivityCausalAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_process_causal_associations", slot_type=ActivityToProcessCausalAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="happens_during", slot_type=HappensDuringAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=ProcessPartOfAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="enabled_by", slot_type=EnabledByAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_input", slot_type=HasInputAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="occurs_in", slot_type=OccursInAssociation, key_name="object", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(DomainEntity):
    """
    An instance of a GO biological process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess
    class_class_curie: ClassVar[str] = "gocam:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    type: Union[str, OntologyClassId] = None
    occurs_in: Optional[Union[Union[dict, "OccursInAssociation"], List[Union[dict, "OccursInAssociation"]]]] = empty_list()
    has_activity_causal_associations: Optional[Union[Union[dict, "ProcessToActivityCausalAssociation"], List[Union[dict, "ProcessToActivityCausalAssociation"]]]] = empty_list()
    has_process_causal_associations: Optional[Union[Union[dict, "ProcessToProcessCausalAssociation"], List[Union[dict, "ProcessToProcessCausalAssociation"]]]] = empty_list()
    happens_during: Optional[Union[Union[dict, "HappensDuringAssociation"], List[Union[dict, "HappensDuringAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="occurs_in", slot_type=OccursInAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_activity_causal_associations", slot_type=ProcessToActivityCausalAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_process_causal_associations", slot_type=ProcessToProcessCausalAssociation, key_name="object", keyed=False)

        self._normalize_inlined_as_list(slot_name="happens_during", slot_type=HappensDuringAssociation, key_name="object", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(DomainEntity):
    """
    An instance of a GO cellular anatomical entity, a cell type, or gross anatomical structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity
    class_class_curie: ClassVar[str] = "gocam:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "AnatomicalEntityCategory"] = None
    part_of: Optional[Union[Union[dict, "AnatomicalPartOfAssociation"], List[Union[dict, "AnatomicalPartOfAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, AnatomicalEntityCategory):
            self.category = AnatomicalEntityCategory(self.category)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=AnatomicalPartOfAssociation, key_name="object", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(DomainEntity):
    """
    An instance of a chemical entity, as defined in CHEBI, including macromolecules defined in NEO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ChemicalEntity
    class_class_curie: ClassVar[str] = "gocam:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationBiomacromolecule(ChemicalEntity):
    """
    This class groups gene, gene product (protein on ncRNA), or a macromolecular complex that is capable of carrying
    out a molecular activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationBiomacromolecule
    class_class_curie: ClassVar[str] = "gocam:InformationBiomacromolecule"
    class_name: ClassVar[str] = "information biomacromolecule"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.InformationBiomacromolecule

    id: Union[str, InformationBiomacromoleculeId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "InformationBiomacromoleculeCategory"] = None
    has_part: Optional[Union[Union[dict, "MacromoleculeHasPartAssociation"], List[Union[dict, "MacromoleculeHasPartAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationBiomacromoleculeId):
            self.id = InformationBiomacromoleculeId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InformationBiomacromoleculeCategory):
            self.category = InformationBiomacromoleculeCategory(self.category)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=MacromoleculeHasPartAssociation, key_name="object", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    """
    An association between a domain entity (e.g. a MolecularActivity) and another domain entity (e.g. another
    MolecularActivity) with evidence and provenance attached
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Association

    object: Union[str, EntityId] = None
    has_evidence: Optional[Union[Dict[Union[str, EvidenceId], Union[dict, "Evidence"]], List[Union[dict, "Evidence"]]]] = empty_dict()
    subject: Optional[Union[str, DomainEntityId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, EntityId):
            self.object = EntityId(self.object)

        self._normalize_inlined_as_list(slot_name="has_evidence", slot_type=Evidence, key_name="id", keyed=True)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class OccursInAssociation(Association):
    """
    An association owned by a MA or BP that connect to an AE object in which the activity/process is carried out
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation
    class_class_curie: ClassVar[str] = "gocam:OccursInAssociation"
    class_name: ClassVar[str] = "occurs in association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.OccursInAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociation(Association):
    """
    An association owned by an upstream MA or BP that connects to a downstream MA or BP. The nature of the causal
    relationship is indicated with the predicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociation
    class_class_curie: ClassVar[str] = "gocam:CausalAssociation"
    class_name: ClassVar[str] = "causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.CausalAssociation

    object: Union[str, ActivityOrProcessId] = None
    subject: Optional[Union[str, DomainEntityId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociationToActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToActivity
    class_class_curie: ClassVar[str] = "gocam:CausalAssociationToActivity"
    class_name: ClassVar[str] = "causal association to activity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.CausalAssociationToActivity

    object: Union[str, MolecularActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociationToProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToProcess
    class_class_curie: ClassVar[str] = "gocam:CausalAssociationToProcess"
    class_name: ClassVar[str] = "causal association to process"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.CausalAssociationToProcess

    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ActivityToActivityCausalAssociation(CausalAssociation):
    """
    A causal association between two molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityToActivityCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ActivityToActivityCausalAssociation"
    class_name: ClassVar[str] = "activity to activity causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ActivityToActivityCausalAssociation

    object: Union[str, MolecularActivityId] = None
    subject: Optional[Union[str, MolecularActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        if self.subject is not None and not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ProcessToProcessCausalAssociation(CausalAssociation):
    """
    A causal association between two biological processes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessToProcessCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessToProcessCausalAssociation"
    class_name: ClassVar[str] = "process to process causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ProcessToProcessCausalAssociation

    object: Union[str, BiologicalProcessId] = None
    subject: Optional[Union[str, BiologicalProcessId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ProcessToActivityCausalAssociation(CausalAssociation):
    """
    A causal association between a biological process and a molecular activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessToActivityCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessToActivityCausalAssociation"
    class_name: ClassVar[str] = "process to activity causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ProcessToActivityCausalAssociation

    object: Union[str, MolecularActivityId] = None
    subject: Optional[Union[str, BiologicalProcessId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ActivityToProcessCausalAssociation(CausalAssociation):
    """
    A causal association between a molecular activity and a biological process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityToProcessCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ActivityToProcessCausalAssociation"
    class_name: ClassVar[str] = "activity to process causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ActivityToProcessCausalAssociation

    object: Union[str, BiologicalProcessId] = None
    subject: Optional[Union[str, MolecularActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class HasPartAssociation(Association):
    """
    General grouping for associations that Link an entity to its parts by a HasPartAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:HasPartAssociation"
    class_name: ClassVar[str] = "has part association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.HasPartAssociation

    object: Union[str, EntityId] = None

@dataclass
class MacromoleculeHasPartAssociation(HasPartAssociation):
    """
    Connects a macromolecule (such as a protein complex) to its parts (gene products or chemical entities)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MacromoleculeHasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:MacromoleculeHasPartAssociation"
    class_name: ClassVar[str] = "macromolecule has part association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.MacromoleculeHasPartAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class PartOfAssociation(Association):
    """
    General grouping for associations that Link an entity to its wholes by a PartOfAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:PartOfAssociation"
    class_name: ClassVar[str] = "part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.PartOfAssociation

    object: Union[str, EntityId] = None

@dataclass
class AnatomicalPartOfAssociation(PartOfAssociation):
    """
    Connects an anatomical entity (such as a component, cell, or gross anatomical entity) to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:AnatomicalPartOfAssociation"
    class_name: ClassVar[str] = "anatomical part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.AnatomicalPartOfAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ProcessPartOfAssociation(PartOfAssociation):
    """
    Connects a MA or BP to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessPartOfAssociation"
    class_name: ClassVar[str] = "process part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ProcessPartOfAssociation

    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EnabledByAssociation(Association):
    """
    Connects an MA to the information biomacromolecule that executes the activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation
    class_class_curie: ClassVar[str] = "gocam:EnabledByAssociation"
    class_name: ClassVar[str] = "enabled by association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.EnabledByAssociation

    object: Union[str, InformationBiomacromoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, InformationBiomacromoleculeId):
            self.object = InformationBiomacromoleculeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HappensDuringAssociation(Association):
    """
    Connects an MF to a process or phase in which the process occurs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation
    class_class_curie: ClassVar[str] = "gocam:HappensDuringAssociation"
    class_name: ClassVar[str] = "happens during association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.HappensDuringAssociation

    object: Union[str, ActivityOrProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HasInputAssociation(Association):
    """
    Connects an MF or BP to its input entity, which may be a chemical entity, an information biomacromolecule, or a
    larger structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation
    class_class_curie: ClassVar[str] = "gocam:HasInputAssociation"
    class_name: ClassVar[str] = "has input association"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.HasInputAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OntologyClass
    class_class_curie: ClassVar[str] = "gocam:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[str, CategoryType] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CategoryType):
            self.category = CategoryType(self.category)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationEntity(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationEntity
    class_class_curie: ClassVar[str] = "gocam:InformationEntity"
    class_name: ClassVar[str] = "information entity"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.InformationEntity

    id: Union[str, InformationEntityId] = None

@dataclass
class Publication(InformationEntity):
    """
    A published entity such as a paper in pubmed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Publication
    class_class_curie: ClassVar[str] = "gocam:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Publication

    id: Union[str, PublicationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Evidence(InformationEntity):
    """
    An instance of a piece of evidence. Evidence attributes such as type, reference, hang off of here
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Evidence
    class_class_curie: ClassVar[str] = "gocam:Evidence"
    class_name: ClassVar[str] = "evidence"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Evidence

    id: Union[str, EvidenceId] = None
    evidence_type: Union[str, OntologyClassId] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    reference: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    with_object: Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceId):
            self.id = EvidenceId(self.id)

        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.reference]

        if not isinstance(self.with_object, list):
            self.with_object = [self.with_object] if self.with_object is not None else []
        self.with_object = [v if isinstance(v, EntityId) else EntityId(v) for v in self.with_object]

        super().__post_init__(**kwargs)


@dataclass
class DomainEntityMixin(YAMLRoot):
    """
    Grouping for mixins that apply to GO-CAM entities. These mixins allow us to group together entities that are alike
    in some fashion
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainEntityMixin
    class_class_curie: ClassVar[str] = "gocam:DomainEntityMixin"
    class_name: ClassVar[str] = "domain entity mixin"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.DomainEntityMixin

    id: Union[str, DomainEntityMixinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainEntityMixinId):
            self.id = DomainEntityMixinId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ActivityOrProcess(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityOrProcess
    class_class_curie: ClassVar[str] = "gocam:ActivityOrProcess"
    class_name: ClassVar[str] = "activity or process"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ActivityOrProcess

    id: Union[str, ActivityOrProcessId] = None

@dataclass
class ProcessOrPhase(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessOrPhase
    class_class_curie: ClassVar[str] = "gocam:ProcessOrPhase"
    class_name: ClassVar[str] = "process or phase"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.ProcessOrPhase

    id: Union[str, ProcessOrPhaseId] = None

@dataclass
class Continuant(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Continuant
    class_class_curie: ClassVar[str] = "gocam:Continuant"
    class_name: ClassVar[str] = "continuant"
    class_model_uri: ClassVar[URIRef] = GOCAM_QUERIES.Continuant

    id: Union[str, ContinuantId] = None

# Enumerations
class ModelStateEnum(EnumDefinitionImpl):

    production = PermissibleValue(text="production")
    development = PermissibleValue(text="development")

    _defn = EnumDefinition(
        name="ModelStateEnum",
    )

class AnatomicalEntityCategory(EnumDefinitionImpl):

    CellularAnatomicalEntity = PermissibleValue(text="CellularAnatomicalEntity")
    Cell = PermissibleValue(text="Cell")
    GrossAnatomicalStructure = PermissibleValue(text="GrossAnatomicalStructure")
    Organism = PermissibleValue(text="Organism")

    _defn = EnumDefinition(
        name="AnatomicalEntityCategory",
    )

class InformationBiomacromoleculeCategory(EnumDefinitionImpl):

    GeneOrReferenceProtein = PermissibleValue(text="GeneOrReferenceProtein",
                                                                   meaning=GOCAM_QUERIES["biolink.GeneOrGeneProduct"])
    ProteinIsoform = PermissibleValue(text="ProteinIsoform")
    MacromolecularComplex = PermissibleValue(text="MacromolecularComplex")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="InformationBiomacromoleculeCategory",
    )

class CausalPredicateEnum(EnumDefinitionImpl):

    regulates = PermissibleValue(text="regulates",
                                         meaning=RO["0002211"])

    _defn = EnumDefinition(
        name="CausalPredicateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "causally upstream of, positive effect",
                PermissibleValue(text="causally upstream of, positive effect",
                                 meaning=RO["0002304"]) )
        setattr(cls, "causally upstream of, negative effect",
                PermissibleValue(text="causally upstream of, negative effect",
                                 meaning=RO["0002305"]) )
        setattr(cls, "causally upstream of",
                PermissibleValue(text="causally upstream of",
                                 meaning=RO["0002411"]) )
        setattr(cls, "immediately causally upstream of",
                PermissibleValue(text="immediately causally upstream of",
                                 meaning=RO["0002412"]) )
        setattr(cls, "causally upstream of or within",
                PermissibleValue(text="causally upstream of or within",
                                 meaning=RO["0002418"]) )
        setattr(cls, "causally upstream of or within, negative effect",
                PermissibleValue(text="causally upstream of or within, negative effect",
                                 meaning=RO["0004046"]) )
        setattr(cls, "causally upstream of or within, positive effect",
                PermissibleValue(text="causally upstream of or within, positive effect",
                                 meaning=RO["0004047"]) )
        setattr(cls, "negatively regulates",
                PermissibleValue(text="negatively regulates",
                                 meaning=RO["0002212"]) )
        setattr(cls, "positively regulates",
                PermissibleValue(text="positively regulates",
                                 meaning=RO["0002213"]) )

# Slots
class slots:
    pass

slots.aggregate_count = Slot(uri=GOCAM_QUERIES.aggregate_count, name="aggregate_count", curie=GOCAM_QUERIES.curie('aggregate_count'),
                   model_uri=GOCAM_QUERIES.aggregate_count, domain=None, range=Optional[int])

slots.model_count = Slot(uri=GOCAM_QUERIES.model_count, name="model_count", curie=GOCAM_QUERIES.curie('model_count'),
                   model_uri=GOCAM_QUERIES.model_count, domain=None, range=Optional[int])

slots.activity_count = Slot(uri=GOCAM_QUERIES.activity_count, name="activity_count", curie=GOCAM_QUERIES.curie('activity_count'),
                   model_uri=GOCAM_QUERIES.activity_count, domain=None, range=Optional[int])

slots.minimum_connected_entity_count = Slot(uri=GOCAM_QUERIES.minimum_connected_entity_count, name="minimum_connected_entity_count", curie=GOCAM_QUERIES.curie('minimum_connected_entity_count'),
                   model_uri=GOCAM_QUERIES.minimum_connected_entity_count, domain=None, range=Optional[int])

slots.title_regex = Slot(uri=GOCAM_QUERIES.title_regex, name="title_regex", curie=GOCAM_QUERIES.curie('title_regex'),
                   model_uri=GOCAM_QUERIES.title_regex, domain=None, range=Optional[str])

slots.graph = Slot(uri=GOCAM_QUERIES.graph, name="graph", curie=GOCAM_QUERIES.curie('graph'),
                   model_uri=GOCAM_QUERIES.graph, domain=None, range=Optional[str])

slots.results = Slot(uri=RESULTSET.results, name="results", curie=RESULTSET.curie('results'),
                   model_uri=GOCAM_QUERIES.results, domain=None, range=Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]])

slots.binding_key = Slot(uri=RESULTSET.binding_key, name="binding_key", curie=RESULTSET.curie('binding_key'),
                   model_uri=GOCAM_QUERIES.binding_key, domain=None, range=URIRef)

slots.binding_value = Slot(uri=RESULTSET.binding_value, name="binding_value", curie=RESULTSET.curie('binding_value'),
                   model_uri=GOCAM_QUERIES.binding_value, domain=None, range=Optional[str])

slots.query_template = Slot(uri=RESULTSET.query_template, name="query_template", curie=RESULTSET.curie('query_template'),
                   model_uri=GOCAM_QUERIES.query_template, domain=None, range=Optional[str])

slots.bindings = Slot(uri=RESULTSET.bindings, name="bindings", curie=RESULTSET.curie('bindings'),
                   model_uri=GOCAM_QUERIES.bindings, domain=None, range=Optional[Union[Dict[Union[str, BindingBindingKey], Union[dict, Binding]], List[Union[dict, Binding]]]])

slots.id = Slot(uri=GOCAM.id, name="id", curie=GOCAM.curie('id'),
                   model_uri=GOCAM_QUERIES.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=GOCAM_QUERIES.name, domain=None, range=Optional[Union[str, LabelType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=GOCAM_QUERIES.type, domain=None, range=Union[str, OntologyClassId])

slots.category = Slot(uri=GOCAM.category, name="category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM_QUERIES.category, domain=None, range=Union[str, CategoryType])

slots.with_object = Slot(uri=LEGO.evidence, name="with object", curie=LEGO.curie('evidence'),
                   model_uri=GOCAM_QUERIES.with_object, domain=None, range=Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]])

slots.reference = Slot(uri=DCE.source, name="reference", curie=DCE.curie('source'),
                   model_uri=GOCAM_QUERIES.reference, domain=None, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.provided_by = Slot(uri=PAV.providedBy, name="provided_by", curie=PAV.curie('providedBy'),
                   model_uri=GOCAM_QUERIES.provided_by, domain=None, range=Optional[str])

slots.contributor = Slot(uri=DCE.contributor, name="contributor", curie=DCE.curie('contributor'),
                   model_uri=GOCAM_QUERIES.contributor, domain=None, range=Optional[Union[str, List[str]]])

slots.date = Slot(uri=DCE.date, name="date", curie=DCE.curie('date'),
                   model_uri=GOCAM_QUERIES.date, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=GOCAM.evidence_type, name="evidence type", curie=GOCAM.curie('evidence_type'),
                   model_uri=GOCAM_QUERIES.evidence_type, domain=None, range=Union[str, OntologyClassId],
                   pattern=re.compile(r'^ECO:\d+$'))

slots.type_inferences = Slot(uri=GOCAM.type_inferences, name="type inferences", curie=GOCAM.curie('type_inferences'),
                   model_uri=GOCAM_QUERIES.type_inferences, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.related_to = Slot(uri=GOCAM.related_to, name="related to", curie=GOCAM.curie('related_to'),
                   model_uri=GOCAM_QUERIES.related_to, domain=None, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])

slots.occurs_in = Slot(uri=GOCAM.occurs_in, name="occurs in", curie=GOCAM.curie('occurs_in'),
                   model_uri=GOCAM_QUERIES.occurs_in, domain=None, range=Optional[Union[Union[dict, OccursInAssociation], List[Union[dict, OccursInAssociation]]]])

slots.has_causal_associations = Slot(uri=GOCAM.has_causal_associations, name="has causal associations", curie=GOCAM.curie('has_causal_associations'),
                   model_uri=GOCAM_QUERIES.has_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociation], List[Union[dict, CausalAssociation]]]])

slots.has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="has activity causal associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM_QUERIES.has_activity_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociationToActivity], List[Union[dict, CausalAssociationToActivity]]]])

slots.has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="has process causal associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM_QUERIES.has_process_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociationToProcess], List[Union[dict, CausalAssociationToProcess]]]])

slots.happens_during = Slot(uri=GOCAM.happens_during, name="happens during", curie=GOCAM.curie('happens_during'),
                   model_uri=GOCAM_QUERIES.happens_during, domain=None, range=Optional[Union[Union[dict, HappensDuringAssociation], List[Union[dict, HappensDuringAssociation]]]])

slots.part_of = Slot(uri=GOCAM.part_of, name="part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM_QUERIES.part_of, domain=None, range=Optional[Union[Union[dict, PartOfAssociation], List[Union[dict, PartOfAssociation]]]])

slots.has_part = Slot(uri=GOCAM.has_part, name="has part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM_QUERIES.has_part, domain=None, range=Optional[Union[Union[dict, HasPartAssociation], List[Union[dict, HasPartAssociation]]]])

slots.enabled_by = Slot(uri=RO['0002333'], name="enabled by", curie=RO.curie('0002333'),
                   model_uri=GOCAM_QUERIES.enabled_by, domain=MolecularActivity, range=Optional[Union[Union[dict, "EnabledByAssociation"], List[Union[dict, "EnabledByAssociation"]]]])

slots.has_input = Slot(uri=GOCAM.has_input, name="has input", curie=GOCAM.curie('has_input'),
                   model_uri=GOCAM_QUERIES.has_input, domain=None, range=Optional[Union[Union[dict, HasInputAssociation], List[Union[dict, HasInputAssociation]]]])

slots.has_evidence = Slot(uri=GOCAM.has_evidence, name="has evidence", curie=GOCAM.curie('has_evidence'),
                   model_uri=GOCAM_QUERIES.has_evidence, domain=Association, range=Optional[Union[Dict[Union[str, EvidenceId], Union[dict, "Evidence"]], List[Union[dict, "Evidence"]]]])

slots.association_slot = Slot(uri=GOCAM.association_slot, name="association slot", curie=GOCAM.curie('association_slot'),
                   model_uri=GOCAM_QUERIES.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.subject, domain=Association, range=Optional[Union[str, DomainEntityId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.object, domain=Association, range=Union[str, EntityId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM_QUERIES.predicate, domain=Association, range=Optional[Union[str, PredicateType]])

slots.model_property = Slot(uri=GOCAM.model_property, name="model property", curie=GOCAM.curie('model_property'),
                   model_uri=GOCAM_QUERIES.model_property, domain=None, range=Optional[str])

slots.title = Slot(uri=DCE.title, name="title", curie=DCE.curie('title'),
                   model_uri=GOCAM_QUERIES.title, domain=None, range=Optional[str])

slots.state = Slot(uri=LEGO.modelstate, name="state", curie=LEGO.curie('modelstate'),
                   model_uri=GOCAM_QUERIES.state, domain=None, range=Optional[Union[str, "ModelStateEnum"]])

slots.domain_entity_set = Slot(uri=GOCAM.domain_entity_set, name="domain entity set", curie=GOCAM.curie('domain_entity_set'),
                   model_uri=GOCAM_QUERIES.domain_entity_set, domain=None, range=Optional[Union[Dict[Union[str, DomainEntityId], Union[dict, DomainEntity]], List[Union[dict, DomainEntity]]]])

slots.molecular_activity_set = Slot(uri=GOCAM.molecular_activity_set, name="molecular activity set", curie=GOCAM.curie('molecular_activity_set'),
                   model_uri=GOCAM_QUERIES.molecular_activity_set, domain=None, range=Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, MolecularActivity]], List[Union[dict, MolecularActivity]]]])

slots.biological_process_set = Slot(uri=GOCAM.biological_process_set, name="biological process set", curie=GOCAM.curie('biological_process_set'),
                   model_uri=GOCAM_QUERIES.biological_process_set, domain=None, range=Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, BiologicalProcess]], List[Union[dict, BiologicalProcess]]]])

slots.information_biomacromolecule_set = Slot(uri=GOCAM.information_biomacromolecule_set, name="information biomacromolecule set", curie=GOCAM.curie('information_biomacromolecule_set'),
                   model_uri=GOCAM_QUERIES.information_biomacromolecule_set, domain=None, range=Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, InformationBiomacromolecule]], List[Union[dict, InformationBiomacromolecule]]]])

slots.chemical_entity_set = Slot(uri=GOCAM.chemical_entity_set, name="chemical entity set", curie=GOCAM.curie('chemical_entity_set'),
                   model_uri=GOCAM_QUERIES.chemical_entity_set, domain=None, range=Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], List[Union[dict, ChemicalEntity]]]])

slots.ontology_class_set = Slot(uri=GOCAM.ontology_class_set, name="ontology class set", curie=GOCAM.curie('ontology_class_set'),
                   model_uri=GOCAM_QUERIES.ontology_class_set, domain=None, range=Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, OntologyClass]], List[Union[dict, OntologyClass]]]])

slots.model_query_results = Slot(uri=RESULTSET.results, name="model query_results", curie=RESULTSET.curie('results'),
                   model_uri=GOCAM_QUERIES.model_query_results, domain=ModelQuery, range=Optional[Union[Union[str, ModelId], List[Union[str, ModelId]]]])

slots.molecular_activity_part_of = Slot(uri=GOCAM.part_of, name="molecular activity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM_QUERIES.molecular_activity_part_of, domain=MolecularActivity, range=Optional[Union[Union[dict, "ProcessPartOfAssociation"], List[Union[dict, "ProcessPartOfAssociation"]]]])

slots.molecular_activity_has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="molecular activity_has activity causal associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM_QUERIES.molecular_activity_has_activity_causal_associations, domain=MolecularActivity, range=Optional[Union[Union[dict, "ActivityToActivityCausalAssociation"], List[Union[dict, "ActivityToActivityCausalAssociation"]]]])

slots.molecular_activity_has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="molecular activity_has process causal associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM_QUERIES.molecular_activity_has_process_causal_associations, domain=MolecularActivity, range=Optional[Union[Union[dict, "ActivityToProcessCausalAssociation"], List[Union[dict, "ActivityToProcessCausalAssociation"]]]])

slots.biological_process_has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="biological process_has activity causal associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM_QUERIES.biological_process_has_activity_causal_associations, domain=BiologicalProcess, range=Optional[Union[Union[dict, "ProcessToActivityCausalAssociation"], List[Union[dict, "ProcessToActivityCausalAssociation"]]]])

slots.biological_process_has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="biological process_has process causal associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM_QUERIES.biological_process_has_process_causal_associations, domain=BiologicalProcess, range=Optional[Union[Union[dict, "ProcessToProcessCausalAssociation"], List[Union[dict, "ProcessToProcessCausalAssociation"]]]])

slots.anatomical_entity_category = Slot(uri=GOCAM.category, name="anatomical entity_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM_QUERIES.anatomical_entity_category, domain=AnatomicalEntity, range=Union[str, "AnatomicalEntityCategory"])

slots.anatomical_entity_part_of = Slot(uri=GOCAM.part_of, name="anatomical entity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM_QUERIES.anatomical_entity_part_of, domain=AnatomicalEntity, range=Optional[Union[Union[dict, "AnatomicalPartOfAssociation"], List[Union[dict, "AnatomicalPartOfAssociation"]]]])

slots.information_biomacromolecule_category = Slot(uri=GOCAM.category, name="information biomacromolecule_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM_QUERIES.information_biomacromolecule_category, domain=InformationBiomacromolecule, range=Union[str, "InformationBiomacromoleculeCategory"])

slots.information_biomacromolecule_has_part = Slot(uri=GOCAM.has_part, name="information biomacromolecule_has part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM_QUERIES.information_biomacromolecule_has_part, domain=InformationBiomacromolecule, range=Optional[Union[Union[dict, "MacromoleculeHasPartAssociation"], List[Union[dict, "MacromoleculeHasPartAssociation"]]]])

slots.occurs_in_association_object = Slot(uri=RDF.object, name="occurs in association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.occurs_in_association_object, domain=OccursInAssociation, range=Union[str, AnatomicalEntityId])

slots.causal_association_subject = Slot(uri=RDF.subject, name="causal association_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.causal_association_subject, domain=CausalAssociation, range=Optional[Union[str, DomainEntityId]])

slots.causal_association_object = Slot(uri=RDF.object, name="causal association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.causal_association_object, domain=CausalAssociation, range=Union[str, ActivityOrProcessId])

slots.causal_association_predicate = Slot(uri=RDF.predicate, name="causal association_predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM_QUERIES.causal_association_predicate, domain=CausalAssociation, range=Optional[Union[str, PredicateType]])

slots.causal_association_to_activity_object = Slot(uri=RDF.object, name="causal association to activity_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.causal_association_to_activity_object, domain=None, range=Union[str, MolecularActivityId])

slots.causal_association_to_process_object = Slot(uri=RDF.object, name="causal association to process_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.causal_association_to_process_object, domain=None, range=Union[str, BiologicalProcessId])

slots.activity_to_activity_causal_association_subject = Slot(uri=RDF.subject, name="activity to activity causal association_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.activity_to_activity_causal_association_subject, domain=ActivityToActivityCausalAssociation, range=Optional[Union[str, MolecularActivityId]])

slots.activity_to_activity_causal_association_object = Slot(uri=RDF.object, name="activity to activity causal association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.activity_to_activity_causal_association_object, domain=ActivityToActivityCausalAssociation, range=Union[str, MolecularActivityId])

slots.process_to_process_causal_association_subject = Slot(uri=RDF.subject, name="process to process causal association_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.process_to_process_causal_association_subject, domain=ProcessToProcessCausalAssociation, range=Optional[Union[str, BiologicalProcessId]])

slots.process_to_process_causal_association_object = Slot(uri=RDF.object, name="process to process causal association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.process_to_process_causal_association_object, domain=ProcessToProcessCausalAssociation, range=Union[str, BiologicalProcessId])

slots.process_to_activity_causal_association_subject = Slot(uri=RDF.subject, name="process to activity causal association_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.process_to_activity_causal_association_subject, domain=ProcessToActivityCausalAssociation, range=Optional[Union[str, BiologicalProcessId]])

slots.process_to_activity_causal_association_object = Slot(uri=RDF.object, name="process to activity causal association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.process_to_activity_causal_association_object, domain=ProcessToActivityCausalAssociation, range=Union[str, MolecularActivityId])

slots.activity_to_process_causal_association_subject = Slot(uri=RDF.subject, name="activity to process causal association_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM_QUERIES.activity_to_process_causal_association_subject, domain=ActivityToProcessCausalAssociation, range=Optional[Union[str, MolecularActivityId]])

slots.activity_to_process_causal_association_object = Slot(uri=RDF.object, name="activity to process causal association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.activity_to_process_causal_association_object, domain=ActivityToProcessCausalAssociation, range=Union[str, BiologicalProcessId])

slots.macromolecule_has_part_association_object = Slot(uri=RDF.object, name="macromolecule has part association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.macromolecule_has_part_association_object, domain=MacromoleculeHasPartAssociation, range=Union[str, ContinuantId])

slots.anatomical_part_of_association_object = Slot(uri=RDF.object, name="anatomical part of association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.anatomical_part_of_association_object, domain=AnatomicalPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.process_part_of_association_object = Slot(uri=RDF.object, name="process part of association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.process_part_of_association_object, domain=ProcessPartOfAssociation, range=Union[str, BiologicalProcessId])

slots.enabled_by_association_object = Slot(uri=RDF.object, name="enabled by association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.enabled_by_association_object, domain=EnabledByAssociation, range=Union[str, InformationBiomacromoleculeId])

slots.happens_during_association_object = Slot(uri=RDF.object, name="happens during association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.happens_during_association_object, domain=HappensDuringAssociation, range=Union[str, ActivityOrProcessId])

slots.has_input_association_object = Slot(uri=RDF.object, name="has input association_object", curie=RDF.curie('object'),
                   model_uri=GOCAM_QUERIES.has_input_association_object, domain=HasInputAssociation, range=Union[str, ContinuantId])

# Auto generated from config_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-07T11:13:12
# Schema: config_schema
#
# id: https://linkml.io/sparqlfun/config_schema
# description: Schema for configuration
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CONFIG_SCHEMA = CurieNamespace('config_schema', 'https://linkml.io/sparqlfun/config_schema')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RESULTSET = CurieNamespace('resultset', 'https://linkml.io/sparqlfun/resultset')
DEFAULT_ = CONFIG_SCHEMA


# Types

# Class references
class EndpointName(extended_str):
    pass


class ProfileName(extended_str):
    pass


class BindingBindingKey(extended_str):
    pass


@dataclass
class SystemConfiguration(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIG_SCHEMA.SystemConfiguration
    class_class_curie: ClassVar[str] = "config_schema:SystemConfiguration"
    class_name: ClassVar[str] = "SystemConfiguration"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.SystemConfiguration

    endpoints: Optional[Union[Dict[Union[str, EndpointName], Union[dict, "Endpoint"]], List[Union[dict, "Endpoint"]]]] = empty_dict()
    profiles: Optional[Union[Dict[Union[str, ProfileName], Union[dict, "Profile"]], List[Union[dict, "Profile"]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="endpoints", slot_type=Endpoint, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="profiles", slot_type=Profile, key_name="name", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Endpoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIG_SCHEMA.Endpoint
    class_class_curie: ClassVar[str] = "config_schema:Endpoint"
    class_name: ClassVar[str] = "Endpoint"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.Endpoint

    name: Union[str, EndpointName] = None
    url: str = None
    type_property: Optional[str] = None
    example_queries: Optional[Union[Union[dict, "ExampleQuery"], List[Union[dict, "ExampleQuery"]]]] = empty_list()
    implements: Optional[Union[Union[str, ProfileName], List[Union[str, ProfileName]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EndpointName):
            self.name = EndpointName(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.type_property is not None and not isinstance(self.type_property, str):
            self.type_property = str(self.type_property)

        if not isinstance(self.example_queries, list):
            self.example_queries = [self.example_queries] if self.example_queries is not None else []
        self.example_queries = [v if isinstance(v, ExampleQuery) else ExampleQuery(**as_dict(v)) for v in self.example_queries]

        if not isinstance(self.implements, list):
            self.implements = [self.implements] if self.implements is not None else []
        self.implements = [v if isinstance(v, ProfileName) else ProfileName(v) for v in self.implements]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ExampleQuery(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIG_SCHEMA.ExampleQuery
    class_class_curie: ClassVar[str] = "config_schema:ExampleQuery"
    class_name: ClassVar[str] = "ExampleQuery"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.ExampleQuery

    query_template: Optional[str] = None
    bindings: Optional[Union[Dict[Union[str, BindingBindingKey], Union[dict, "Binding"]], List[Union[dict, "Binding"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.query_template is not None and not isinstance(self.query_template, str):
            self.query_template = str(self.query_template)

        self._normalize_inlined_as_dict(slot_name="bindings", slot_type=Binding, key_name="binding_key", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Profile(YAMLRoot):
    """
    A feature implemented by an endpoint for supporting certain kinds of queries
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIG_SCHEMA.Profile
    class_class_curie: ClassVar[str] = "config_schema:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.Profile

    name: Union[str, ProfileName] = None
    description: Optional[str] = None
    subsets: Optional[Union[str, List[str]]] = empty_list()
    modules: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ProfileName):
            self.name = ProfileName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.subsets, list):
            self.subsets = [self.subsets] if self.subsets is not None else []
        self.subsets = [v if isinstance(v, str) else str(v) for v in self.subsets]

        if not isinstance(self.modules, list):
            self.modules = [self.modules] if self.modules is not None else []
        self.modules = [v if isinstance(v, str) else str(v) for v in self.modules]

        super().__post_init__(**kwargs)


class GenericResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.GenericResult
    class_class_curie: ClassVar[str] = "resultset:GenericResult"
    class_name: ClassVar[str] = "GenericResult"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.GenericResult


@dataclass
class ResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.ResultSet
    class_class_curie: ClassVar[str] = "resultset:ResultSet"
    class_name: ClassVar[str] = "ResultSet"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.ResultSet

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
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.Binding

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


# Enumerations


# Slots
class slots:
    pass

slots.endpoints = Slot(uri=CONFIG_SCHEMA.endpoints, name="endpoints", curie=CONFIG_SCHEMA.curie('endpoints'),
                   model_uri=CONFIG_SCHEMA.endpoints, domain=None, range=Optional[Union[Dict[Union[str, EndpointName], Union[dict, Endpoint]], List[Union[dict, Endpoint]]]])

slots.name = Slot(uri=CONFIG_SCHEMA.name, name="name", curie=CONFIG_SCHEMA.curie('name'),
                   model_uri=CONFIG_SCHEMA.name, domain=None, range=URIRef)

slots.url = Slot(uri=CONFIG_SCHEMA.url, name="url", curie=CONFIG_SCHEMA.curie('url'),
                   model_uri=CONFIG_SCHEMA.url, domain=None, range=str)

slots.description = Slot(uri=CONFIG_SCHEMA.description, name="description", curie=CONFIG_SCHEMA.curie('description'),
                   model_uri=CONFIG_SCHEMA.description, domain=None, range=Optional[str])

slots.type_property = Slot(uri=CONFIG_SCHEMA.type_property, name="type_property", curie=CONFIG_SCHEMA.curie('type_property'),
                   model_uri=CONFIG_SCHEMA.type_property, domain=None, range=Optional[str])

slots.example_queries = Slot(uri=CONFIG_SCHEMA.example_queries, name="example_queries", curie=CONFIG_SCHEMA.curie('example_queries'),
                   model_uri=CONFIG_SCHEMA.example_queries, domain=None, range=Optional[Union[Union[dict, ExampleQuery], List[Union[dict, ExampleQuery]]]])

slots.profiles = Slot(uri=CONFIG_SCHEMA.profiles, name="profiles", curie=CONFIG_SCHEMA.curie('profiles'),
                   model_uri=CONFIG_SCHEMA.profiles, domain=None, range=Optional[Union[Dict[Union[str, ProfileName], Union[dict, Profile]], List[Union[dict, Profile]]]])

slots.implements = Slot(uri=CONFIG_SCHEMA.implements, name="implements", curie=CONFIG_SCHEMA.curie('implements'),
                   model_uri=CONFIG_SCHEMA.implements, domain=None, range=Optional[Union[Union[str, ProfileName], List[Union[str, ProfileName]]]])

slots.subsets = Slot(uri=CONFIG_SCHEMA.subsets, name="subsets", curie=CONFIG_SCHEMA.curie('subsets'),
                   model_uri=CONFIG_SCHEMA.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.modules = Slot(uri=CONFIG_SCHEMA.modules, name="modules", curie=CONFIG_SCHEMA.curie('modules'),
                   model_uri=CONFIG_SCHEMA.modules, domain=None, range=Optional[Union[str, List[str]]])

slots.results = Slot(uri=RESULTSET.results, name="results", curie=RESULTSET.curie('results'),
                   model_uri=CONFIG_SCHEMA.results, domain=None, range=Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]])

slots.binding_key = Slot(uri=RESULTSET.binding_key, name="binding_key", curie=RESULTSET.curie('binding_key'),
                   model_uri=CONFIG_SCHEMA.binding_key, domain=None, range=URIRef)

slots.binding_value = Slot(uri=RESULTSET.binding_value, name="binding_value", curie=RESULTSET.curie('binding_value'),
                   model_uri=CONFIG_SCHEMA.binding_value, domain=None, range=Optional[str])

slots.query_template = Slot(uri=RESULTSET.query_template, name="query_template", curie=RESULTSET.curie('query_template'),
                   model_uri=CONFIG_SCHEMA.query_template, domain=None, range=Optional[str])

slots.bindings = Slot(uri=RESULTSET.bindings, name="bindings", curie=RESULTSET.curie('bindings'),
                   model_uri=CONFIG_SCHEMA.bindings, domain=None, range=Optional[Union[Dict[Union[str, BindingBindingKey], Union[dict, Binding]], List[Union[dict, Binding]]]])

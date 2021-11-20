# Auto generated from config_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-19T17:37:54
# Schema: config_schema
#
# id: https://w3id.org/sparqlfun/config_schema
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
CONFIG_SCHEMA = CurieNamespace('config_schema', 'https://w3id.org/sparqlfun/config_schema')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CONFIG_SCHEMA


# Types

# Class references
class EndpointName(extended_str):
    pass


@dataclass
class SystemConfiguration(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIG_SCHEMA.SystemConfiguration
    class_class_curie: ClassVar[str] = "config_schema:SystemConfiguration"
    class_name: ClassVar[str] = "SystemConfiguration"
    class_model_uri: ClassVar[URIRef] = CONFIG_SCHEMA.SystemConfiguration

    endpoints: Optional[Union[Dict[Union[str, EndpointName], Union[dict, "Endpoint"]], List[Union[dict, "Endpoint"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="endpoints", slot_type=Endpoint, key_name="name", keyed=True)

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

slots.type_property = Slot(uri=CONFIG_SCHEMA.type_property, name="type_property", curie=CONFIG_SCHEMA.curie('type_property'),
                   model_uri=CONFIG_SCHEMA.type_property, domain=None, range=Optional[str])

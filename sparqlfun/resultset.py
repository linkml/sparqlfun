# Auto generated from resultset.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-22T16:07:22
# Schema: sparqlfun-resultset
#
# id: https://linkml.io/sparqlfun/resultset
# description: SPARQL Query Result Model
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


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RESULTSET = CurieNamespace('resultset', 'https://linkml.io/sparqlfun/resultset')
DEFAULT_ = RESULTSET


# Types

# Class references



class GenericResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.GenericResult
    class_class_curie: ClassVar[str] = "resultset:GenericResult"
    class_name: ClassVar[str] = "GenericResult"
    class_model_uri: ClassVar[URIRef] = RESULTSET.GenericResult


@dataclass
class ResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RESULTSET.ResultSet
    class_class_curie: ClassVar[str] = "resultset:ResultSet"
    class_name: ClassVar[str] = "ResultSet"
    class_model_uri: ClassVar[URIRef] = RESULTSET.ResultSet

    results: Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, GenericResult) else GenericResult(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.results = Slot(uri=RESULTSET.results, name="results", curie=RESULTSET.curie('results'),
                   model_uri=RESULTSET.results, domain=None, range=Optional[Union[Union[dict, GenericResult], List[Union[dict, GenericResult]]]])

import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import *

logging.basicConfig(level=logging.DEBUG)


def test_config():
    se = SparqlEngine(endpoint='ubergraph')
    e = se.get_endpoint()
    print(f'E={e}')
    for exq in e.example_queries:
        print(f'EXAMPLE: {exq.query_template} // {exq.bindings}')
        for k, v in exq.bindings.items():
            print(f'  {k} = {v.binding_value}')

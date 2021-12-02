import pytest
import logging

from sparqlfun.query_engine import SparqlEngine
from sparqlfun.model import BloodVesselSubcategory

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture(autouse=True)
def engine():
    se = SparqlEngine(endpoint='ontobee')
    return se

def test_enum():
    e = BloodVesselSubcategory('vein')
    print(e)

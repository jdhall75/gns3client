"""
Tests for `gns3client` module.
"""
import pytest
from gns3client import api

@pytest.fixture()
def client():
    api.base_url = 'http://localhost:3080'
    return api

def test_api_appliances(client):
    response = client.appliance.get_appliances()
    assert response.status_code == 200

# import pytest module
import pytest

# import app
from app import app

import pandas as pd


@pytest.fixture
def client():
    return app.test_client()


# testing home route with get
def test_table(client):
    response = client.get('/')
    assert response.status_code == 200


# testing home route with post method
def test_bad_table(client):
    response = client.post('/')
    assert response.status_code == 405

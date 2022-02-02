from web import app
from flask import json, jsonify

import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert {"status":"success","msg":"Hello World"} == json.loads(response.get_data(as_text=True))
import json
import os

import pytest

from backend import create_app
from backend.routes import routes


@pytest.fixture
def client():
    """Creates a Flask test client for unit testing."""
    app = create_app()
    app.config["TESTING"] = True  # Enable test mode
    with app.test_client() as client:
        yield client


def load_json(filename):
    """Helper function to load JSON from a file."""
    with open(f"{filename}", "r") as file:
        return json.load(file)


def test_release_created_valid_payload(client):
    """Test API with a valid GitHub webhook payload."""
    os.environ['WEBHOOK_SECRET'] = 'hello_test'
    response = routes.verify_signature(load_json("test_webhook_payload.json"), os.getenv("WEBHOOK_SECRET"), "sha1=b92b840189af47f1d9a4a6b48555be3ee47bc9ae")
    assert response == True

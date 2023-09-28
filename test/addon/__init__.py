import pytest
from api.addon import app


@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    client = app.test_client()
    yield client

    # clean up / reset resources here

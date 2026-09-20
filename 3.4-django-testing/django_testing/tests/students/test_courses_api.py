import pytest

from tests.conftest import students, courses, client

@pytest.mark.django_db
def test_example(client, courses):
    course = courses()
    client = client()
    resp = client.get("api/v1/")


    assert resp.status_code == 201

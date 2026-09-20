
import pytest
from model_bakery import baker
from  rest_framework.test import APIClient

@pytest.mark.fixture
def client():
    return APIClient()

@pytest.mark.fixture
def courses():
    def course(*args, **kwargs):
        return baker.make(*args, **kwargs)
    return course

@pytest.mark.fixture
def students():
    def student(*args, **kwargs):
        return baker.make(*args, **kwargs)
    return student



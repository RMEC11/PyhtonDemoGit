import pytest


@pytest.fixture(scope="class")
def setup():
    print("Executing before method")
    yield
    print("Executing after method")

@pytest.fixture()
def datLoad():
    print("User Profile created")
    return["Abhishek", "Tiwari", "embibe.com"]
@pytest.fixture(params=[("chrome","Abhishek", "Tiwari"),("Firefox", "Tiwari", "Abhishek"),("IE", "embibe.com")])
def crossbrowser(request):
    return request.param
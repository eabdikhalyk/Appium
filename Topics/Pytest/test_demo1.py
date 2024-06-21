import pytest

@pytest.fixture(scope='module')
def setUpClass():
    print("Before a Class -------")
    yield
    print("After a Class -------")


@pytest.fixture()
def setUp(setUpClass):
    print()
    print("setUp method, start Before a method")
    yield
    print("After a method")

def test_methodA( setUp):
    print('method A')

def test_methodB(setUp):
    print('method B')
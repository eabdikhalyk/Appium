import pytest

def test_method_A():
    print("This is method A")

def test_method_B():
    print("This is method B")

@pytest.mark.skip
def test_method_C():
    print("This is method C")

def test_method_D():
    print("This is method D")
    assert False
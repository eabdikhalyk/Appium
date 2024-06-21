import pytest
import allure

def test_method_A():
    allureLogs("Launching app")
    allureLogs("This a Method A Step - 1")
    allureLogs("This a Method A Step - 2p")
    print("This is method A")

def test_method_B():
    print("This is method B")

@pytest.mark.skip
def test_method_C():
    print("This is method C")

def test_method_D():
    print("This is method D")
    assert False

def allureLogs(text):
    with allure.step(text):
        pass
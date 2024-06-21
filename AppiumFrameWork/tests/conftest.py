import time
import pytest
from AppiumFrameWork.base.DriverClass import Driver

@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before a Class -------")
    driver = Driver().getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After a Class -------")


@pytest.fixture()
def beforeMethod():
    print()
    print("setUp method, start Before a method")
    yield
    print("After a method")
import unittest
import pytest
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.pages.LoginPage import LoginPage
from AppiumFrameWork.base.BasePage import BasePage

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_LoginFailMethod(self):
        cl.allureLogs("App Openned")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginButton()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order=2)
    def test_openLoginScreen(self):
        self.bp.kayCode(4)
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginButton()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order = 3)
    def test_enterDataInForm(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()


from AppiumFrameWork.base.BasePage import  BasePage
from AppiumFrameWork.utilities import  CustomLogger as cl

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _loginButton = "com.skill2lead.appiumdemo:id/Login" # id
    _enterEmail = "3" # index
    _enterPassword = "Enter Password" # text
    _clickLoginButton = "com.skill2lead.appiumdemo:id/Btn3" # id

    _wrongCredentials = "Wrong Credentials" # text
    _pageTitle = "Enter Admin" # text
    _enterText = "com.skill2lead.appiumdemo:id/Edt_admin" # id
    _submitButton = "SUBMIT" # text

    def clickLoginButton(self):
        self.clickElement(self._loginButton,"id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self):
        self.sendText("admin@gmail.com", self._enterEmail,"3")
        cl.allureLogs("Entered email id")

    def enterPassword(self):
        self.sendText("admin123",self._enterPassword,"text")
        cl.allureLogs("Entered Password")
    def enterInvalidPassword(self):
        self.sendText("admin12344",self._enterPassword,"text")
        cl.allureLogs("Entered Password")
    def clickOnLoginButton(self):
        self.clickElement(self._clickLoginButton,"id")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle, "text")
        assert adminScreen == True
        cl.allureLogs("Openned Admin Screen")

    def enterText(self):
        self.sendText("Erke2Code", self._enterText,"id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit Button")

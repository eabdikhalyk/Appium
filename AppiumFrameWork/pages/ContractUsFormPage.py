from AppiumFrameWork.base.BasePage import  BasePage
from AppiumFrameWork.utilities import  CustomLogger as cl

class ContractForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    _contractFromButton = "com.skill2lead.appiumdemo:id/ContactUs" # id
    _pageTitle = "Contact Us form" # text
    _enterName = "Enter Name" # text
    _enterEmail = "Enter Email" # text
    _enterAddress = "Enter Address" # text
    _enterMobileNumber = "4" # index number
    _submitButton = "SUBMIT" # text

    def clickContactFormButton(self):
        self.clickElement(self._contractFromButton, "id")
        cl.allureLogs("Clicked on Contract us From Button")
    def verifyContractPage(self):
        element = self.isDisplayed(self._pageTitle,"text")
        assert element == True
        cl.allureLogs("Contract us From page opened")

    def enterName(self):
        self.sendText('Yerkebulan',self._enterName,"text")
        cl.allureLogs("Enter Name")
    def enterEmail(self):
        self.sendText("erke@mail.com",self._enterEmail, "text")
        cl.allureLogs("Enter Email")
    def enterAddress(self):
        self.sendText("Kazakhstan, Shymkent, Baidibek bi", self._enterAddress,"text")
        cl.allureLogs("Enter Address")
    def enterNumber(self):
        self.sendText("87001201212","ABC","index")
        cl.allureLogs("Enter Number")
    def clickSubmit(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit button")
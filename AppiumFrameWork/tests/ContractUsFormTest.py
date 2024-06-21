import unittest
import pytest
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.pages.ContractUsFormPage import ContractForm

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContractFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContractForm(self.driver)

    @pytest.mark.run(order=1)
    def test_openContractForm(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContractPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterNumber()
        self.cf.clickSubmit()




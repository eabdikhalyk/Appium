import time
import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import AppiumFrameWork.utilities.CustomLogger as cl
class BasePage:
    log = cl.customLogger()
    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self,locatorValue,locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,
                                                                                 ElementNotSelectableException,
                                                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x:x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x:x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         'UiSelector().description("%s")' % (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         'UiSelector().index(%d)' % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x:x.find_element(AppiumBy.XPATH,'%s' % (locatorValue)))
            return element
        else:
            self.log.info('Locator value ' + locatorValue + ' not found')

        return element

    def getElement(self,locatorValue,locatorType = "id"):
        element =None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            self.log.info("Element found with locatorType: "+
                          locatorType+ " with locatorValue: "+locatorValue)
        except:
            self.log.info("Element not found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("Clicked on element found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue)
        except:
            self.log.info(
                "Unable to element not found with locatorType: " +
                locatorType + " and with locatorValue: " + locatorValue)

        return element

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info("Send text on element found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue)
        except:
            self.log.info("Unable send text to element not found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue)
        self.takeScreenshot(locatorType)
        assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info("Element found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue +" is displayed")
            return True
        except:
            self.log.info("Element not found with locatorType: " +
                          locatorType + " and with locatorValue: " + locatorValue+" is not displayed")
            return False

    def screenShot(self, screenShotName):
        fileName = screenShotName + "_"+ (time.strftime("%d%m%y%H%M%S"))+".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path: " + screenshotPath)
        except:
            self.log.info("Unable to save to Path: " + screenshotPath)

    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self,value):
        self.driver.press_key(value)
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])
ele = wait.until(lambda x:x.find_element(AppiumBy.ID,'com.skill2lead.appiumdemo:id/ScrollView'))
ele.click()

wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON15"))'))
btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("BUTTON15")')
btn.click()
time.sleep(3)
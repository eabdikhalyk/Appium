from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# Step 4 : Using explicit wait create a variable for a button
ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("TAB ACTIVITY"))'))
btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("TAB ACTIVITY")')
# Step 5 : Create the object the TouchAction class and call tap() method
actions = TouchAction(driver)
actions.tap(None, 576, 1296, 1)
actions.perform()

time.sleep(2)
driver.quit()
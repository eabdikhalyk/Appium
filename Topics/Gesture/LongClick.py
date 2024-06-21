from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])
ele = wait.until(lambda x:x.find_element(AppiumBy.ID,'com.skill2lead.appiumdemo:id/LongClick'))
actions = TouchAction(driver)
actions.long_press(ele,5)
actions.perform()

time.sleep(2)
driver.quit()
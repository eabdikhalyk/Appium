from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])
wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
btn = driver.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/drag")
btn.click()

drag_btn = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/btnDrag"))
element_lay = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/layout3"))
actions = TouchAction(driver)
actions.long_press(drag_btn).move_to(element_lay).release().perform()
time.sleep(2)
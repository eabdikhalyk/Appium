import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
ele_index.click()
time.sleep(5)


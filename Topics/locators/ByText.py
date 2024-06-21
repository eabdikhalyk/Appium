import desired_caps
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
button_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ENTER SOME VALUE")')
# button_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ENTER SOME VALUE")')
button_text.click()



import desired_caps
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()

content = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("Btn1")')
content.click()
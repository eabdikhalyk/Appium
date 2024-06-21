from Topics.locators import desired_caps
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
element = driver.find_element(AppiumBy.ID,'com.skill2lead.appiumdemo:id/EnterValue')
print("Is display: ", element.is_displayed())
print("Is Enable: ", element.is_enabled())
print('Is Selected: ', element.is_selected())
print('Size: ', element.size)
print('Location: ', element.location)
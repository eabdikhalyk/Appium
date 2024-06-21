from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
driver.implicitly_wait(15)

element_id = driver.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/EnterValue")
element_id.click()

time.sleep(2)
driver.quit()


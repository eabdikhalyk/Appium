from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
element_id = driver.find_element(AppiumBy.ID,'com.skill2lead.appiumdemo:id/EnterValue')
print('Text on the Button: ', element_id.text)
print('Text on the Button: ', element_id.get_attribute('text'))
print('Content Des of the Button: ', element_id.get_attribute('content-desc'))
element_id.click()

time.sleep(2)

element_class = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
element_class.send_keys("Skell2Lead")
time.sleep(2)
element_class.clear()
time.sleep(2)
element_class.send_keys('Skill2Lead')
time.sleep(2)

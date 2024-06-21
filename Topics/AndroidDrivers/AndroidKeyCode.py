from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
button_className = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.Button")
button_className.click()
time.sleep(2)

edit_className = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText").send_keys("test")
edit_className.click()
driver.press_keycode(67)
driver.press_keycode(67)
time.sleep(2)
driver.press_keycode(4)
driver.press_keycode(4)
time.sleep(2)
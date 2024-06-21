import desired_caps
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()

elements = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
text = 'ScrollView'
for element in elements:
    if text == element.text:
        element.click()
        break

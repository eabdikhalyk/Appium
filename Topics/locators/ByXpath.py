import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
# xpath_1 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn3"]')
# xpath_1.click()
# xpath_2 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.skill2lead.appiumdemo:id/ScrollView"]')
# xpath_2.click()
xpath_3 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ScrollView"]')
xpath_3.click()
time.sleep(2)
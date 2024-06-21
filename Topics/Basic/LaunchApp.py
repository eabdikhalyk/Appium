import time

import appium.webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = "13"
desired_caps['deviceName'] = "Galaxy S10 Lite"
desired_caps['app'] = ('C:/Users/Yerkebulan/AndroidProjects/apk/Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options, direct_connection=True)

ele_id = driver.find_element(AppiumBy.ID,'com.skill2lead.appiumdemo:id/EnterValue')
ele_id.click()
time.sleep(5)


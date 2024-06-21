from appium import webdriver
import time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['automationName']='UiAutomator2'
desired_caps['platformVersion']='11'
desired_caps['deviceName']='Pixel3XL'
desired_caps['app']=('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage']='com.code2lead.kwad'
desired_caps['appActivity']='com.code2lead.kwad.MainActivity'
desired_caps['fullReset']=True

time.sleep(5)

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

time.sleep(5)
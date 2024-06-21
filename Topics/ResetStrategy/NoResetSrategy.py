from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='11'
desired_caps['deviceName']='Pixel'
desired_caps['app']=('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage']='com.android.chrome'
desired_caps['appActivity']='com.google.android.apps.chrome.Main'
desired_caps['noReset']=True

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
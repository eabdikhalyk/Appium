from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Topics.locators import desired_caps
import time
from appium.webdriver.common.appiumby import AppiumBy

driver = desired_caps.getDriver()
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])
ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("TAB ACTIVITY")'))
ele.click()
deviceSize = driver.get_window_size()
print("Device Width and Height : ",deviceSize)
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

startx = screenWidth*8/9
endx = screenWidth/9
starty = screenHeight/2
endy = screenHeight/2

# *********** Right to Left ************* #
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2


actions = TouchAction(driver)

# Step 7 : perform the action swiping from left to Right
actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()

# Step 8 : perform the action swiping from Right to Left
actions.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()

time.sleep(2)
driver.quit()

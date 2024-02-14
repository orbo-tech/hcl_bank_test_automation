from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def swipe_to_element_by_accessibility_id(appium_driver, element_id, start_x, start_y):
    """
    Swipe to a specified element using Appium's TouchAction.

    Parameters:
    - driver: Appium WebDriver instance.
    - element_id (str): The ID of the element to swipe to.
    """
    # Find the element to which you want to swipe
    element = WebDriverWait(appium_driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, element_id)))

    # Create a TouchAction object
    actions = TouchAction(appium_driver)

    # To Perform the swipe
    actions.press(x=element.location[start_x],
                  y=element.location[start_y]).move_to(x=0, y=-100).release().perform()


def find_element_by_accessibility_id(appium_driver, element_id):
    element = WebDriverWait(appium_driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, element_id)))
    return element


def find_element_by_xpath(appium_driver, element_id):
    element = WebDriverWait(appium_driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, element_id)))
    return element

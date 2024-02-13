from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BS_USERNAME = "rajveera_Zveoqa"
BS_ACCESS_KEY = "rW2oJB2HTXawKEQwADFC"
IPA_APP_ID = "bs://<app-id>"
APK_APP_ID = "bs://4861e1a441291a028b8f336b6c718ba913fa6cc1"
ios_options = XCUITestOptions().load_capabilities({
    # Set URL of the application under test
    "app": IPA_APP_ID,

    # Specify device and os_version for testing
    "deviceName": "iPhone 11 Pro",
    "platformName": "ios",
    "platformVersion": "13",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : BS_USERNAME,
        "accessKey" : BS_ACCESS_KEY,
        "projectName" : "TenantEv",
        "buildName" : "tenantev-ios-build-1",
        "sessionName" : "BStack first_test"
    }
})
android_options = UiAutomator2Options().load_capabilities({
    # Set URL of the application under test
    "app": APK_APP_ID,

    # Specify device and os_version for testing
    "deviceName": "google pixel 3",
    "platformName": "android",
    "platformVersion": "9.0",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : BS_USERNAME,
        "accessKey" : BS_ACCESS_KEY,
        "projectName" : "TenantEv",
        "buildName" : "tenantev-android-build-1",
        "sessionName" : "BStack first_test"
    }
})
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=android_options)


time.sleep(15)
# Click English language button option
english_language_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_english_btn")))
english_language_button.click()



# # wait for carousel to rotate and get started button to active
# time.sleep(10)
#
# # Click Get started button
# get_started_button = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@content-desc='Get Started']")))
# get_started_button.click()
#
#
# # Enter email in sign up page
# email_text_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_email_field")))
# email_text_input.send_keys("test@browserstack.com")
#
# # Enter password in sign up page
# password_text_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_password_field")))
# password_text_input.send_keys("Password@1")
#
# # Enter confirm password in sign up page
# confirm_password_text_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_confirm_password_field")))
# email_text_input.send_keys("Password@1")
#
# # Click Continue button
# continue_button = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_create_account_button")))
# continue_button.click()
#
# # Get Face ID page text
# face_id_page_title = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "tenant_ev_scan_my_face"))
# )
#
# # Assert user successfully land on Face ID page.
# assert face_id_page_title.text == "Set up Face ID"
#
# driver.quit()

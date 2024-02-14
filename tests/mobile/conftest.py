import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from helpers.utils import get_json_value


credentials = get_json_value("../../test_credentials/credentials.json", "browserstack")


@pytest.fixture
def appium_driver(request):
    """
    Fixture to set up and tear down the Appium driver.
    """

    android_options = UiAutomator2Options().load_capabilities({
        # Set URL of the application under test
        "app": credentials["app_id"],

        # Specify device and os_version for testing
        "deviceName": "google pixel 3a",
        "platformName": "android",
        "platformVersion": "9.0",

        # Set other BrowserStack capabilities
        "bstack:options": {
            "userName": credentials["username"],
            "accessKey": credentials["access_key"],
            "projectName": "TenantEv",
            "buildName": "hcl-android-build-1",
            "sessionName": "BrowserStack Test:1"
        }
    })
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=android_options)
    return driver


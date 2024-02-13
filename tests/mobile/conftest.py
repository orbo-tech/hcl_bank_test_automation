import pytest
from appium import webdriver

@pytest.fixture
def appium_driver(request):
    """
    Fixture to set up and tear down the Appium driver.
    """
    desired_capabilities = {
        'platformName': 'Android',  # or 'iOS'
        'deviceName': 'your_device_name',
        'appPackage': 'your_app_package',
        'appActivity': 'your_app_activity',
        'automationName': 'UiAutomator2',  # or 'XCUITest' for iOS
        # Add other desired capabilities as needed
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def fin():
        """
        Teardown method to quit the driver after the test.
        """
        driver.quit()

    request.addfinalizer(fin)

    return driver

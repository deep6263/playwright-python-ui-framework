import pytest
from config.config import config
import allure


@pytest.mark.smoke
def test_saucedemo_title(page):
    """
    Test to verify the title of the SauceDemo website.
    This test uses the 'page' fixture to interact with the browser page.
    """
    page.goto("/")
    assert page.title() == "Swag Labs"

@allure.story("Environment configuration is loaded correctly")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_environment_configuration():
    """
    Test to verify that the environment configuration is loaded correctly.
    This test checks the base URL and environment name from the configuration.
    """

    assert config.base_url == "https://www.saucedemo.com/"
    assert config.environment == "qa"




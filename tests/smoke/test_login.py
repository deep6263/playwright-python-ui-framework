import pytest
import allure
from pages.login_page import LoginPage
from utils.data_loader import load_json


users = load_json("users.json")

@allure.epic("SauceDemo UI Automation")
@allure.feature("Login")
class TestLogin:
    @allure.story("Valid user login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize("user", users["validUsers"])
    def test_valid_login(self, page, user):
        """Verify that valid users can log in successfully."""

        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(
            user["username"],
            user["password"]
        )

        assert "inventory" in page.url
    @allure.story("Invalid user login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("user", users["invalidUsers"])
    def test_invalid_login(self, page, user):
        """Verify that invalid users cannot log in."""

        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(
            user["username"],
            user["password"]
        )

        error_message = login_page.get_error_message()

        assert "Username and password do not match" in error_message
   
    @allure.story("Locked user cannot login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("user", users["lockedUsers"])
    def test_locked_user_login(self, page, user):
        """Verify that locked users cannot log in."""

        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(
            user["username"],
            user["password"]
        )

        error_message = login_page.get_error_message()

        assert "locked out" in error_message.lower()
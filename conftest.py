import pytest
from playwright.sync_api import BrowserContext, Page
from config.config import config
from pages.login_page import LoginPage
from utils.data_loader import load_json
import allure

@pytest.fixture
def context(browser) -> BrowserContext:
    context = browser.new_context(
        base_url=config.base_url
    )

    yield context

    context.close()

@pytest.fixture
def page(
    context: BrowserContext,
    request,
    ) -> Page:
    """
    Fixture to create a new page for each test.
    Captures a screenshot and attaches it to Allure if the test fails.
    """

    page = context.new_page()

    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    page.close()

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """
    Fixture to create a new page and log in before each test.
    This fixture is scoped to the function, meaning it will be created
    and destroyed for each test function that uses it.
    """

    users = load_json("users.json")
    valid_user = users["validUsers"][0]

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        valid_user["username"],
        valid_user["password"]
    )

    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test execution results on the test item."""

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)
    
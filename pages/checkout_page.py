from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for SauceDemo checkout flow."""

    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page: Page):
        super().__init__(page)

    def enter_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """Enter customer information."""

        self.page.locator(self.FIRST_NAME_INPUT).fill(first_name)
        self.page.locator(self.LAST_NAME_INPUT).fill(last_name)
        self.page.locator(self.POSTAL_CODE_INPUT).fill(postal_code)

    def continue_to_overview(self) -> None:
        """Continue from customer information to order overview."""

        self.page.locator(self.CONTINUE_BUTTON).click()

    def finish_order(self) -> None:
        """Complete the order."""

        self.page.locator(self.FINISH_BUTTON).click()

    def cancel_checkout(self) -> None:
        """Cancel checkout."""

        self.page.locator(self.CANCEL_BUTTON).click()

    def get_confirmation_message(self) -> str:
        """Return the order confirmation message."""

        return self.page.locator(self.COMPLETE_HEADER).inner_text()

    def get_error_message(self) -> str:
        """Return the checkout validation error message."""

        return self.page.locator(
            "[data-test='error']"
        ).inner_text()

        
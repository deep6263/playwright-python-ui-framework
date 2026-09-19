from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for SauceDemo shopping cart."""

    CART_ITEMS = ".cart_item"
    CART_ITEM_NAMES = ".inventory_item_name"
    REMOVE_BUTTON = "button[id^='remove-']"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_cart_items(self) -> list[str]:
        """Return the names of products currently in the cart."""
        return self.page.locator(self.CART_ITEM_NAMES).all_inner_texts()


    def wait_for_cart_items(self) -> None:
        """Wait until cart items are visible."""
        self.page.locator(self.CART_ITEMS).first.wait_for(
            state="visible"
        )


    def get_cart_item_count(self) -> int:
        """Return the number of products currently in the cart."""
        return self.page.locator(self.CART_ITEMS).count()

    def remove_product(self, product_name: str) -> None:
        """Remove a specific product from the cart."""

        item = self.page.locator(
            self.CART_ITEMS,
            has=self.page.locator(
                self.CART_ITEM_NAMES,
                has_text=product_name
            )
        )

        item.locator(self.REMOVE_BUTTON).click()

    def checkout(self) -> None:
        """Proceed to checkout."""
        self.page.locator(self.CHECKOUT_BUTTON).click()

    def continue_shopping(self) -> None:
        """Return to the products page."""
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()
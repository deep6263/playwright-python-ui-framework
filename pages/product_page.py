from playwright.sync_api import Page
from pages.base_page import BasePage 


class ProductPage(BasePage):

    PRODUCT_TITLE = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = ".product_sort_container"
    PRODUCT_NAMES = ".inventory_item_name"
    PRODUCT_PRICES = ".inventory_item_price"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_product_names(self) -> list[str]:
        """Get the names of all products on the page."""
        return self.page.locator(self.PRODUCT_TITLE).all_inner_texts()

    def get_product_prices(self) -> list[str]:
        """Get the prices of all products on the page."""
        return self.page.locator(self.PRODUCT_PRICE).all_inner_texts()

    def add_product_to_cart(self, product_name: str) -> None:
        """Add a product to the cart by its name."""
        product = self.page.locator(
            ".inventory_item",
            has=self.page.locator(
                self.PRODUCT_TITLE,
                has_text=product_name
            )
        )

        product.locator("button[id^='add-to-cart']").click()

    def get_cart_count(self) -> int:
        """Return the number of items currently in the cart."""

        badge = self.page.locator(self.CART_BADGE)

        if not badge.is_visible():
            return 0

        return int(badge.inner_text())

    def open_cart(self) -> None:
        """Open the shopping cart."""

        self.page.locator(self.CART_LINK).click()

    def sort_products(self, sort_option: str) -> None:
        """Sort products using the product sorting dropdown."""

        self.page.locator(self.SORT_DROPDOWN).select_option(sort_option)


    def get_first_product_name(self) -> str:
        """Return the first product name displayed."""

        return self.page.locator(self.PRODUCT_NAMES).first.inner_text()


    def get_first_product_price(self) -> str:
        """Return the first product price displayed."""

        return self.page.locator(self.PRODUCT_PRICES).first.inner_text()
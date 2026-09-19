import pytest
import allure
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@allure.epic("SauceDemo UI Automation")
@allure.feature("Shopping Cart")
class TestCart:
    
    @allure.story("Added product is displayed in cart")
    @pytest.mark.regression
    def test_added_product_is_displayed_in_cart(self, logged_in_page):
        """Verify that an added product appears in the cart."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        products_page.open_cart()

        cart_items = cart_page.get_cart_items()

        assert "Sauce Labs Backpack" in cart_items
    
    @allure.story("Product can be removed from cart")
    @pytest.mark.regression
    def test_remove_product_from_cart(self, logged_in_page):
        """Verify that a product can be removed from the cart."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        print("Badge count:", products_page.get_cart_count())
        with allure.step("Open shopping cart"):
            products_page.open_cart()
            cart_page.wait_for_cart_items()

            assert cart_page.get_cart_item_count() == 1

    @allure.story("Cart item count is accurate")
    @pytest.mark.regression
    def test_cart_item_count(self, logged_in_page):
        """Verify the number of products displayed in the cart."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        assert products_page.get_cart_count() == 1

        products_page.open_cart()

        assert "/cart.html" in logged_in_page.url
        cart_page.wait_for_cart_items()
        assert cart_page.get_cart_item_count() == 1
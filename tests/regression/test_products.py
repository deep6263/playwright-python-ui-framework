import pytest
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.data_loader import load_json

users = load_json("users.json")

@allure.epic("SauceDemo UI Automation")
@allure.feature("Products")
class TestProducts:

    @allure.story("Products are displayed")
    @pytest.mark.regression
    def test_product_are_displayed(self, logged_in_page):
        """Verify that products are displayed after a successful login."""

        product_page = ProductPage(logged_in_page)

        products = product_page.get_product_names()

        assert len(products) > 0

    @allure.story("Product can be added to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_add_product_to_cart(self, logged_in_page):
        """Verify that a product can be added to the cart."""

        product_page = ProductPage(logged_in_page)

        # Use a valid user for login
        valid_user = users["validUsers"][0]

       

        product_name = product_page.get_product_names()[0]
        with allure.step("Add product to cart"):
            product_page.add_product_to_cart(
                product_name
            )
            assert product_page.get_cart_count() == 1

    @allure.story("Products can be sorted by price")
    @pytest.mark.regression
    def test_sort_products_by_price_low_to_high(self, logged_in_page):
        """Verify products can be sorted by price from low to high."""

        products_page = ProductPage(logged_in_page)

        products_page.sort_products("lohi")

        first_price = products_page.get_first_product_price()

        assert first_price == "$7.99"
        
    @allure.story("Product information is displayed")
    @pytest.mark.regression
    def test_product_information_is_displayed(self, logged_in_page):
        """Verify that product name and price are displayed."""

        products_page = ProductPage(logged_in_page)

        product_names = products_page.get_product_names()
        product_prices = products_page.get_product_prices()

        assert len(product_names) > 0
        assert len(product_prices) > 0
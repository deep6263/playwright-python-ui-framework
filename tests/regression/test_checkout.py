import pytest
import allure
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

@allure.epic("SauceDemo UI Automation")
@allure.feature("Checkout")
class TestCheckout:
    @allure.story("Complete checkout successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_complete_checkout(self, logged_in_page):
        """Verify that a user can successfully complete an order."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)
        checkout_page = CheckoutPage(logged_in_page)

        # Add product
        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        assert products_page.get_cart_count() == 1

        # Open cart
        products_page.open_cart()

        cart_page.wait_for_cart_items()

        assert cart_page.get_cart_item_count() == 1

        # Start checkout
        with allure.step("Start checkout"):
            cart_page.checkout()

        # Enter customer information
        with allure.step("Enter customer information"):
            checkout_page.enter_customer_information(
                first_name="Deepesh",
                last_name="Kushwah",
                postal_code="201001",
            )

        checkout_page.continue_to_overview()

        # Finish order
        with allure.step("Complete order"):
            checkout_page.finish_order()

        # Verify confirmation
        with allure.step("Verify order confirmation"):
            confirmation_message = (
                checkout_page.get_confirmation_message()
            )

            assert confirmation_message == "Thank you for your order!"

    @allure.story("Checkout requires first name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_checkout_requires_first_name(self, logged_in_page):
        """Verify that checkout requires a first name."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)
        checkout_page = CheckoutPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        products_page.open_cart()
        cart_page.wait_for_cart_items()
        cart_page.checkout()

        checkout_page.enter_customer_information(
            first_name="",
            last_name="Kushwah",
            postal_code="201001",
        )
        with allure.step("Continue to order overview"):
            checkout_page.continue_to_overview()

        error_message = checkout_page.get_error_message()

        assert "First Name is required" in error_message

    @allure.story("Checkout requires last name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_checkout_requires_last_name(self, logged_in_page):
        """Verify that checkout requires a last name."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)
        checkout_page = CheckoutPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        products_page.open_cart()
        cart_page.wait_for_cart_items()
        cart_page.checkout()

        checkout_page.enter_customer_information(
            first_name="Deepesh",
            last_name="",
            postal_code="201001",
        )

        checkout_page.continue_to_overview()

        error_message = checkout_page.get_error_message()

        assert "Last Name is required" in error_message

    @allure.story("Checkout requires postal code")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_checkout_requires_postal_code(self, logged_in_page):
        """Verify that checkout requires a postal code."""

        products_page = ProductPage(logged_in_page)
        cart_page = CartPage(logged_in_page)
        checkout_page = CheckoutPage(logged_in_page)

        products_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        products_page.open_cart()
        cart_page.wait_for_cart_items()
        cart_page.checkout()

        checkout_page.enter_customer_information(
            first_name="Deepesh",
            last_name="Kushwah",
            postal_code="",
        )

        checkout_page.continue_to_overview()

        error_message = checkout_page.get_error_message()

        assert "Postal Code is required" in error_message
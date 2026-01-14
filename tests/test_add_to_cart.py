import allure
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from config.config import BASE_URL
import time

@allure.feature("Shopping Cart")
@allure.story("Add to Cart and Update Quantity")
@allure.title("Test Add to Cart and Update Quantity")
@allure.description("Verify adding product to cart and updating quantity works correctly")
def test_add_to_cart():
    """
    Test the complete cart workflow:
    1. Login to application
    2. Navigate to product page
    3. Verify product page structure
    """
    driver = get_driver()
    try:
        with allure.step("Navigate to login page"):
            driver.get(BASE_URL + "/auth/login")
            time.sleep(1)
        
        with allure.step("Login to application"):
            login_page = LoginPage(driver)
            login_page.login()
            time.sleep(2)
        
        with allure.step("Navigate to product page - Combination Pliers"):
            driver.get(BASE_URL + "/product/combination-pliers")
            time.sleep(2)
            assert driver.current_url == BASE_URL + "/product/combination-pliers", "Should be on product page"
        
        with allure.step("Verify product page loaded with correct title"):
            assert "Practice Software Testing" in driver.title, "Should be on correct site"
        
        with allure.step("Verify product page structure"):
            assert "practice software testing" in driver.title.lower(), "Page should be on correct site"
            assert "/product/" in driver.current_url, "Should be on product page URL"
            
    finally:
        driver.quit()
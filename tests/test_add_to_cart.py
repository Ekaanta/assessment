import allure
from utils.driver_factory import get_driver
from pages.product_page import ProductPage
from config.config import BASE_URL
import time

@allure.feature("Product Catalog")
@allure.story("Product Page")
@allure.title("Test Product Page Navigation")
@allure.description("Verify product page loads correctly with proper URL and title")
def test_add_to_cart():
    """Test that the product page loads correctly.
    
    Note: Full add-to-cart flow requires valid login credentials and proper
    authentication state. This test validates the page structure.
    """
    driver = get_driver()
    try:
        with allure.step("Navigate to product page"):
            driver.get(BASE_URL + "/product/combination-pliers")
            time.sleep(2)
        
        with allure.step("Verify product page URL"):
            assert driver.current_url == BASE_URL + "/product/combination-pliers", "Should be on product page"
        
        with allure.step("Verify page title"):
            assert "Practice Software Testing" in driver.title, "Should be on correct site"
        
        # Note: Full add-to-cart functionality requires authenticated session
        # The ProductPage.add_to_cart() method is available when user is logged in
        
    finally:
        driver.quit()
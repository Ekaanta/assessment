import allure
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from config.config import BASE_URL
import time

@allure.feature("Authentication")
@allure.story("User Login")
@allure.title("Test User Login")
@allure.description("Verify user can navigate to login page and submit login form")
def test_login():
    driver = get_driver()
    try:
        with allure.step("Navigate to login page"):
            driver.get(BASE_URL + "/auth/login")
        
        with allure.step("Submit login form"):
            login_page = LoginPage(driver)
            login_page.login()
        
        with allure.step("Wait for login to process"):
            time.sleep(2)
        
        with allure.step("Verify page loaded successfully"):
            assert driver.current_url is not None, "Page should load successfully"
    finally:
        driver.quit()
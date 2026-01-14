import allure
from utils.driver_factory import get_driver
from pages.contact_page import ContactPage

@allure.feature("Contact Form")
@allure.story("Form Submission")
@allure.title("Test Contact Form Submission")
@allure.description("Verify user can fill and submit contact form with all required fields")
def test_contact_form_submission():
    driver = get_driver()
    try:
        contact = ContactPage(driver)
        
        with allure.step("Open contact page"):
            contact.open()
        
        with allure.step("Submit contact form with valid data"):
            contact.submit_valid()
        
        with allure.step("Verify success message appears"):
            success_msg = contact.success_message()
            assert success_msg != "", "Success message should appear"
    finally:
        driver.quit()

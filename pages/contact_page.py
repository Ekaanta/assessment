from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from config.config import BASE_URL

class ContactPage(BasePage):
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL = (By.ID, "email")
    SUBJECT = (By.ID, "subject")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    def open(self):
        self.driver.get(BASE_URL + "/contact")

    def submit_empty(self):
        self.click(self.SUBMIT)

    def submit_valid(self):
        self.type(self.FIRST_NAME, "John")
        self.type(self.LAST_NAME, "Doe")
        self.type(self.EMAIL, "test@gmail.com")
        
        # Select a subject
        subject_select = Select(self.driver.find_element(*self.SUBJECT))
        subject_select.select_by_index(1)  # Select first available subject
        
        # Message with 50+ characters
        message = "This is a test message with enough characters to meet the minimum requirement."
        self.type(self.MESSAGE, message)
        self.click(self.SUBMIT)

    def success_message(self):
        return self.get_text(self.SUCCESS)

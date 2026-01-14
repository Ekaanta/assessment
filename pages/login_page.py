from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL, EMAIL, PASSWORD

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    def login(self):
        self.type(self.EMAIL_INPUT, EMAIL)
        self.type(self.PASSWORD_INPUT, PASSWORD)
        self.click(self.LOGIN_BTN)

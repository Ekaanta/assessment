from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "btn-add-to-cart")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

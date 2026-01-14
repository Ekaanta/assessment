from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.quantity")
    TOTAL_PRICE = (By.CSS_SELECTOR, "td.total-price")

    def update_quantity(self, quantity: int):
        qty_input = self.wait.until(
            EC.presence_of_element_located(self.QUANTITY_INPUT)
        )
        qty_input.clear()
        qty_input.send_keys(str(quantity))

    def total_price(self):
        total = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_PRICE)
        )
        return total.text

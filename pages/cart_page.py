from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/cart.html"
        self.button_cart = (By.ID, "shopping_cart_container")
        self.page_title = (By.CLASS_NAME, "title")
        self.button_checkout = (By.ID, "checkout")
        self.button_remove = (By.ID, "remove-sauce-labs-backpack")
        self.button_continue_shopping = (By.ID, "continue-shopping")

    def open_page(self):
        self.driver.get(self.url)

    def assert_page(self):
        assert self.url in self.driver.current_url
        page_title = self.driver.find_element(*self.page_title).text
        assert page_title == "Your Cart"

    def assert_order(self, product_name, product_price):
        page_title = self.driver.find_element(*self.page_title).text
        assert page_title == "Your Cart"
        EC.visibility_of_element_located((By.XPATH, f"//*[text()='{product_name}']"))
        EC.visibility_of_element_located((By.XPATH, f"//*[text()='{product_price}']"))

    def proceed_checkout(self):
        self.driver.find_element(*self.button_checkout).click()

    def remove_product(self):
        self.driver.find_element(*self.button_remove).click()

    def continue_shopping(self):
        self.driver.find_element(*self.button_continue_shopping).click()
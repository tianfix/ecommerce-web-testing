from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage

class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/checkout-complete.html"
        self.page_title = (By.CLASS_NAME, "title")
        self.icon_success = (By.CLASS_NAME, "pony_express")
        self.txt_thank_you = (By.CLASS_NAME, "complete-header")
        self.txt_description = (By.CLASS_NAME, "complete-text")
        self.button_back_home = (By.ID, "back-to-products")

    def assert_page(self):
        assert self.url in self.driver.current_url
        page_title = self.driver.find_element(*self.page_title).text
        assert page_title == "Checkout: Complete!"

        EC.visibility_of_element_located(self.icon_success)
        EC.visibility_of_element_located(self.txt_thank_you)
        EC.visibility_of_element_located(self.txt_description)
        EC.visibility_of_element_located(self.button_back_home)

    def back_to_home(self):
        self.driver.find_element(*self.button_back_home).click()

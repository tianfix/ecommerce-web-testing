from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/inventory.html"
        self.page_title = (By.ID, "header_container")
        self.button_add_to_cart = (By.XPATH, "//*[contains(@id,'add-to-cart')]")
        self.button_remove_from_cart = (By.XPATH, "//*[contains(@id,'remove')]")
        self.badge_cart = (By.CLASS_NAME, "shopping_cart_badge")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(self.driver)
        login_page.login_process("standard_user", "secret_sauce")
        self.assert_page()

    def assert_page(self):
        assert self.url in self.driver.current_url
        self.driver.find_element(*self.page_title)

    def open_product_detail(self, product_name, product_price):
        self.driver.find_element(By.XPATH, f"//*[text()='{product_name}']").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()='{product_name}']")))
        EC.visibility_of_element_located((By.XPATH, f"//*[text()='{product_price}']"))

    def add_product_to_cart(self):
        # if self.driver.find_element(*self.badge_cart):
        #     current_cart_amount = int(self.driver.find_element(*self.badge_cart).text)
        # else:
        #     current_cart_amount = 0

        self.driver.find_element(*self.button_add_to_cart).click()
        self.driver.find_element(*self.button_remove_from_cart)

    def remove_product_from_cart(self):
        self.driver.find_element(*self.button_remove_from_cart).click()
        self.driver.find_element(*self.button_add_to_cart)


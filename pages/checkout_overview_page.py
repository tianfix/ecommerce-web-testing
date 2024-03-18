from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/checkout-step-two.html"
        self.page_title = (By.CLASS_NAME, "title")
        self.product_name = (By.CLASS_NAME, "inventory_item_name")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")
        self.tax_amount = (By.CLASS_NAME, "summary_tax_label")
        self.total_price = (By.CLASS_NAME, "summary_total_label")
        self.button_finish = (By.ID, "finish")

    def assert_page(self):
        assert self.url in self.driver.current_url
        page_title = self.driver.find_element(*self.page_title).text
        assert page_title == "Checkout: Overview"

    def assert_order(self, expected_product_name, expected_product_price):
        product_name = self.driver.find_element(*self.product_name).text
        product_price = self.driver.find_element(*self.product_price).text.replace("$", "")
        tax_amount = float(self.driver.find_element(*self.tax_amount).text.replace("Tax: $", ""))
        total_price = float(self.driver.find_element(*self.total_price).text.replace("Total: $", ""))

        # Assert Product Name & Price
        assert product_name == expected_product_name
        assert product_price == expected_product_price

        # Assert Total Price
        expected_total_price = tax_amount + float(expected_product_price)
        assert total_price == expected_total_price

    def finish_order(self):
        self.driver.find_element(*self.button_finish).click()
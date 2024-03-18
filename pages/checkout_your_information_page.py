from selenium.webdriver.common.by import By

class CheckoutYourInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/checkout-step-one.html"
        self.page_title = (By.CLASS_NAME, "title")
        self.txt_field_first_name = (By.ID, "first-name")
        self.txt_field_last_name = (By.ID, "last-name")
        self.txt_field_postal_code = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")
        self.button_cancel = (By.ID, "cancel")

    def assert_page(self):
        assert self.url in self.driver.current_url
        page_title = self.driver.find_element(*self.page_title).text
        assert page_title == "Checkout: Your Information"

    def fill_valid_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.txt_field_first_name).send_keys(first_name)
        self.driver.find_element(*self.txt_field_last_name).send_keys(last_name)
        self.driver.find_element(*self.txt_field_postal_code).send_keys(postal_code)

    def proceed_information(self):
        self.driver.find_element(*self.button_continue).click()

    def cancel_checkout(self):
        self.driver.find_element(*self.button_cancel).click()
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.txt_field_username = (By.ID, "user-name")
        self.txt_field_password = (By.ID, "password")
        self.button_login = (By.ID, "login-button")
        self.err_msg = (By.XPATH, "//h3[contains(text(),'Epic sadface')]")

    def open_page(self):
        self.driver.get(self.url)

    def assert_page(self):
        assert self.url in self.driver.current_url

    def login_process(self, username, password):
        self.driver.find_element(*self.txt_field_username).send_keys(username)
        self.driver.find_element(*self.txt_field_password).send_keys(password)
        self.driver.find_element(*self.button_login).click()

    def assert_login_error(self, type):
        match type:
            case "Empty Username":
                assert self.driver.find_element(*self.err_msg).text == "Epic sadface: Username is required"
            case "Empty Password":
                assert self.driver.find_element(*self.err_msg).text == "Epic sadface: Password is required"
            case "Invalid Credential":
                assert self.driver.find_element(
                    *self.err_msg).text == "Epic sadface: Username and password do not match any user in this service"

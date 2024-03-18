import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_your_information_page import CheckoutYourInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

# Product Data
product_name = "Sauce Labs Backpack"
product_price = "29.99"
first_name = "Rara"
last_name = "Lesti"
postal_code = "4321"


def test_add_product_to_cart(driver):
    inventory_page = InventoryPage(driver)

    inventory_page.open_page()
    inventory_page.assert_page()
    inventory_page.open_product_detail(product_name, product_price)
    inventory_page.add_product_to_cart()

def test_remove_product_from_cart(driver):
    inventory_page = InventoryPage(driver)

    inventory_page.open_page()
    inventory_page.assert_page()
    inventory_page.open_product_detail(product_name, product_price)
    inventory_page.add_product_to_cart()
    inventory_page.remove_product_from_cart()

def test_e2e_checkout_process(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_your_information_page = CheckoutYourInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    inventory_page.open_page()
    inventory_page.assert_page()
    inventory_page.open_product_detail(product_name, product_price)
    inventory_page.add_product_to_cart()

    cart_page.open_page()
    cart_page.assert_page()
    cart_page.assert_order(product_name, product_price)
    cart_page.proceed_checkout()

    checkout_your_information_page.assert_page()
    checkout_your_information_page.fill_valid_information(first_name, last_name, postal_code)
    checkout_your_information_page.proceed_information()

    checkout_overview_page.assert_page()
    checkout_overview_page.assert_order(product_name, product_price)
    checkout_overview_page.finish_order()

    checkout_complete_page.assert_page()

def test_continue_shopping_from_cart_page(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.open_page()
    inventory_page.assert_page()
    inventory_page.open_product_detail(product_name, product_price)
    inventory_page.add_product_to_cart()

    cart_page.open_page()
    cart_page.assert_page()
    cart_page.assert_order(product_name, product_price)
    cart_page.continue_shopping()

    inventory_page.assert_page()


def test_back_to_home_after_payment_complete(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_your_information_page = CheckoutYourInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    inventory_page.open_page()
    inventory_page.assert_page()
    inventory_page.open_product_detail(product_name, product_price)
    inventory_page.add_product_to_cart()

    cart_page.open_page()
    cart_page.assert_page()
    cart_page.assert_order(product_name, product_price)
    cart_page.proceed_checkout()

    checkout_your_information_page.assert_page()
    checkout_your_information_page.fill_valid_information(first_name, last_name, postal_code)
    checkout_your_information_page.proceed_information()

    checkout_overview_page.assert_page()
    checkout_overview_page.assert_order(product_name, product_price)
    checkout_overview_page.finish_order()

    checkout_complete_page.assert_page()
    checkout_complete_page.back_to_home()

    inventory_page.assert_page()










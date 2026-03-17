import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from curl import *
from data import *

# session, module, class, function
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()        
        browser = webdriver.Chrome(options=options)
    
    elif request.param == "firefox":
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    
    browser.get(main_site) 
    
    yield browser
    browser.quit()

# создание экземпляра главной страницы
@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)
    
# создание экземпляра страницы Лента Заказов
@pytest.fixture(scope='function')
def order_page(driver):        
    return OrderPage(driver)    

# авторизация пользователя
@pytest.fixture(scope='function')
def login(driver, order_page):
    driver.get(login_site)
    order_page.send_keys_to_input(OrderPageLocators.EMAIL_ENTRY, email)
    order_page.send_keys_to_input(OrderPageLocators.PASSWORD_ENTRY, password)    

    order_page.click_with_js(OrderPageLocators.ENTRY_BUTTON_PAGE_ENTRY)
    order_page.wait_for_element(OrderPageLocators.BUTTON_ORDER)

# создание заказа
@pytest.fixture(scope='function')
def create_order_and_get_number(driver, order_page, login):
    driver.get(main_site)
    order_page.make_burger_and_submit()
    
    number = order_page.get_text_ORDER_NUMBER().strip()
    order_page.click_on_BUTTON_CLOSE()
    return number


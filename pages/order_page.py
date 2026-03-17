import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from curl import *

class OrderPage(BasePage):
    
    @allure.step("Проскроллить и перетянуть элемент булочки в зону сборки бургера")
    def drag_and_drop_bun(self): 
        self.scroll_to_element(MainPageLocators.BUTTON_BUN)       
        self.drag_and_drop_element(MainPageLocators.BUTTON_BUN, MainPageLocators.BUN_ZONE)    

    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_BUTTON_ORDER(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
   
    @allure.step("Получить текст номера заказа")
    def get_text_ORDER_NUMBER(self):    
        self.wait_for_order_number(OrderPageLocators.ORDER_NUMBER)       
        return self.get_text_on_element(OrderPageLocators.ORDER_NUMBER).strip()    
        
    @allure.step("Закрыть окно с номером заказа")
    def click_on_BUTTON_CLOSE(self): 
        self.click_with_js(MainPageLocators.BUTTON_CLOSE)

    @allure.step("Перейти в ленту заказов")
    def click_on_BUTTON_ORDER_FEED(self): 
        self.click_with_js(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Получить текст в списке В работе")
    def get_text_ORDER_IN_PROGRESS(self):
        return self.get_text_on_element(OrderPageLocators.ORDER_IN_PROGRESS)
    
    @allure.step("Получить текст счетчика заказов за сегодня")
    def get_text_COUNTER_TODAY(self):
        return self.get_text_on_element(OrderPageLocators.COUNTER_TODAY)
    
    @allure.step("Получить текст счетчика заказов за все время")
    def get_text_COUNTER_ALL_TIME(self):
        return self.get_text_on_element(OrderPageLocators.COUNTER_ALL_TIME)
    
    @allure.step("Авторизация пользователя")
    def login_user(self, user_email, user_password):
       
        self.click_on_element(OrderPageLocators.ENTRY_BUTTON)        
        self.send_keys_to_input(OrderPageLocators.EMAIL_ENTRY, user_email)
        self.send_keys_to_input(OrderPageLocators.PASSWORD_ENTRY, user_password)        
        self.click_with_js(OrderPageLocators.ENTRY_BUTTON_PAGE_ENTRY)

    @allure.step("Собрать бургер и нажать 'Оформить заказ'")
    def make_burger_and_submit(self):
        from locators.main_page_locators import MainPageLocators        
        self.drag_and_drop_js(MainPageLocators.BUTTON_BUN, MainPageLocators.BUN_ZONE)       
        self.click_with_js(OrderPageLocators.BUTTON_ORDER)

    
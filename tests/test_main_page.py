import allure

from locators.main_page_locators import MainPageLocators
from curl import *

class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_button(self, order_page):    
        order_page.click_BUTTON_CONST() 
        assert order_page.url.strip('/') == main_site.strip('/')

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_click_order_feed_button(self, main_page):
        main_page.click_BUTTON_ORDER_FEED()
        
        assert main_page.url == order_site

    @allure.title("Появление всплывающего окна с деталями ингридиента при клике на ингредиент")
    def test_open_ingredient_window(self, main_page):
        main_page.click_BUTTON_BUN()
        
        assert main_page.get_text_ingridient() == "Краторная булка N-200i"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_window(self, main_page):
        main_page.click_BUTTON_BUN()
        main_page.click_on_element(MainPageLocators.BUTTON_CLOSE)
   
        is_closed = main_page.wait_for_invisibility_of_element(MainPageLocators.WINDOW_BUN)
        assert is_closed

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, main_page):
        main_page.scroll_to_element(MainPageLocators.BUTTON_BUN)        
        count_before = main_page.get_text_on_element(MainPageLocators.BUN_COUNTER)
        
        main_page.drag_and_drop_bun()      
        count_after = main_page.get_text_on_element(MainPageLocators.BUN_COUNTER)

        assert int(count_after) > int(count_before)


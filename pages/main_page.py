import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_BUTTON_CONST(self):
       self.click_with_js(MainPageLocators.BUTTON_CONST)

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_BUTTON_ORDER_FEED(self):
        self.click_with_js(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Проскроллить и кликнуть на ингридиент булочки")
    def click_BUTTON_BUN(self):
        self.scroll_to_element(MainPageLocators.BUTTON_BUN)
        self.click_with_js(MainPageLocators.BUTTON_BUN)
    
    @allure.step("Получить текст открытого окна с ингридиентом")
    def get_text_ingridient(self):
        return self.get_text_on_element(MainPageLocators.TEXT_WINDOW_BUN)
    
    @allure.step("Перетянуть элемент булочки в зону сборки бургера")
    def drag_and_drop_bun(self):        
        self.drag_and_drop_js(MainPageLocators.BUTTON_BUN, MainPageLocators.BUN_ZONE)
    

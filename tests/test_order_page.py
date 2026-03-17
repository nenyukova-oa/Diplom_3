import allure

from curl import *


class TestOrderPage:

    @allure.title("Проверка увеличения счетчика 'Выполнено за все время' после оформления заказа")
    def test_counter_all_time_increases(self, order_page, request):        
        order_page.click_BUTTON_ORDER_FEED()
        initial_count = int(order_page.get_text_COUNTER_ALL_TIME())        
        
        _ = request.getfixturevalue('create_order_and_get_number')         
       
        order_page.click_on_BUTTON_ORDER_FEED()
        new_count = int(order_page.get_text_COUNTER_ALL_TIME())

        assert new_count > initial_count

    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' после оформления заказа")
    def test_counter_today_increases(self, order_page, request):        
        order_page.click_on_BUTTON_ORDER_FEED()
        initial_today_count = int(order_page.get_text_COUNTER_TODAY())        
        
        _ = request.getfixturevalue('create_order_and_get_number')        
        
        order_page.click_on_BUTTON_ORDER_FEED()
        new_today_count = int(order_page.get_text_COUNTER_TODAY())
        assert new_today_count > initial_today_count

    @allure.title("Проверка появления номера заказа в разделе 'В работе' после оформления заказа")
    def test_order_number_appears_in_work_section(self, order_page, create_order_and_get_number):       
        order_number = create_order_and_get_number       
        order_page.click_on_BUTTON_ORDER_FEED()       
        all_in_progress = order_page.get_text_ORDER_IN_PROGRESS()
        
        assert order_number in all_in_progress

    
        


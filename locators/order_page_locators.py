from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    #локаторы для входа в аккаунт
    ENTRY_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" на главной странице
    EMAIL_ENTRY = (By.XPATH, "//h2[text()='Вход']/following-sibling::form//label[text()='Email']/following-sibling::input") #поле "Email" в форме входа
    PASSWORD_ENTRY =(By.XPATH, "//h2[text()='Вход']/following-sibling::form//input[@name='Пароль']") #поле "Пароль" в форме входа
    ENTRY_BUTTON_PAGE_ENTRY = (By.XPATH, "//button[text()='Войти']") #кнопка "Войти" на странице входа  
    
    # Локаторы для создания заказа, главная страница    
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка Оформить заказ
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]") # номер заказа
    
    # Локаторы на странице Лента Заказов
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed')]") # заказ в работе
    COUNTER_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p") # счетчик заказов за сегодня
    COUNTER_ALL_TIME = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p") # счетчик заказов за все время


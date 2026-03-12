from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для кнопок в шапке страницы
    BUTTON_CONST = (By.XPATH, "//li/a[contains(., 'Конструктор')]") # кнопка "Конструктор" вверху страницы
    BUTTON_ORDER_FEED = (By.XPATH, "//li/a[contains(., 'Лента Заказов')]") # кнопка "Лента Заказов" вверху страницы  
    
    # Локаторы для ингридиентов
    BUTTON_BUN = (By.XPATH, "//a[contains(.,'Краторная булка')]") # кнопка Краторная булка N-200i в списке ингридиентов
    WINDOW_BUN = (By.XPATH, "//div[contains(@class, 'Modal_modal__container') and .//h2[contains(text(), 'Детали ингредиента')]]") # окно ингридиента Краторная булка N-200i
    TEXT_WINDOW_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']") # текст ингридиента в окне ингридиента
    BUTTON_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # кнопка для закрытия окна ингридиента    
    BUN_ZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]") # зона для перетягивания булочки
    BUN_COUNTER = (By.XPATH, "//a[contains(.,'Краторная булка')]//p[contains(@class, 'counter')]") # счетчик булочек


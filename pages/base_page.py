import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

TIMEOUT = 5

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Кликнуть на элемент через JavaScript для Firefox")
    def click_with_js(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text
  
    @allure.step("Перетянуть элемент {locator_source} в {locator_target}")
    def drag_and_drop_element(self, locator_source, locator_target, timeout=TIMEOUT):
        source = self.wait_for_element(locator_source, timeout)
        target = self.wait_for_element(locator_target, timeout)    
    
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
    
        actions = ActionChains(self.driver)    
        actions.click_and_hold(source).pause(1.0).move_to_element(target).pause(1.0).release().perform()

    @allure.step("Перетянуть элемент (JS-симуляция для Firefox)")
    def drag_and_drop_js(self, locator_source, locator_target):
        source = self.wait_for_element(locator_source)
        target = self.wait_for_element(locator_target)    
    
        js_script = """
        const source = arguments[0];
        const target = arguments[1];
        const dataTransfer = new DataTransfer();
    
        ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(name => {
            const event = new DragEvent(name, {
                bubbles: true, cancelable: true, dataTransfer
            });
            (name === 'drop' ? target : source).dispatchEvent(event);
         });
        """
        self.driver.execute_script(js_script, source, target)

    @allure.step("Подождать исчезновения элемента")
    def wait_for_invisibility_of_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))  
    
    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
   


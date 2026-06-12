from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_base import *
import allure


class BasePage:

    @allure.step("Создать драйвер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Нажать на элемент")
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Ввести текст")
    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Подождать загрузку элемента")
    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Элемент появился")
    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    @allure.step("Прокрурить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)

    @allure.step("Получить URL")    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Подождать открытия нового окна")
    def wait_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
    
    @allure.step("Перейти в новое окно")
    def switch_to_new_window(self):
        self.wait_new_window()
        self.driver.swith_to.window(self.driver.window_handles[1])

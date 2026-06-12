from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure

class OrderPageScooter(BasePage):
    YANDEX_BUTTON = [By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"]
    SCOOTER_BUTTON = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"]

    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LASTNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]

    @allure.step('Открыть сайт')
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждем загрузки станицы")
    def wait_for_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.NAME))
    
    @allure.step("Вводим имя")
    def input_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)
    
    @allure.step("Вводим фамилию")
    def input_lastname(self, lastname):
        self.driver.find_element(*self.LASTNAME).send_keys(lastname)

    @allure.step("Ввод адреса")
    def input_address(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    @allure.step("Выбор метро")
    def choose_metro(self, station):
        self.driver.find_element(*self.METRO).click()
        metro_station = (By.XPATH,f"//div[contains(@class,'select-search')]//*[contains(text(),'{station}')]")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(metro_station))
        self.driver.find_element(*metro_station).click()
    
    @allure.step("Ввод телефона")
    def input_phone(self, phone):
        self.driver.find_element(*self.PHONE).send_keys(phone)

    @allure.step("Нажать далее")
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step("Заполение формы заказа")
    def full_order (self, name, lastname, address, station, phone):
        self.input_name(name)
        self.input_lastname(lastname)
        self.input_address(address)
        self.choose_metro(station)
        self.input_phone(phone)

    @allure.step("Нажать на лого Самокат")
    def click_scooter(self):
        self.driver.find_element(*self.SCOOTER_BUTTON).click()

    @allure.step("Нажать на лого Яндекс")
    def click_yandex(self):
        self.driver.find_element(*self.YANDEX_BUTTON).click()
    
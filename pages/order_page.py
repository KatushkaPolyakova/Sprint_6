from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.locators_order import *
from locators.locators_base import *
import allure


class OrderPageScooter(BasePage):

    @allure.step('Открыть сайт')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждем загрузки станицы")
    def wait_for_order_page(self):
        self.wait_visibility(NAME)
    
    @allure.step("Вводим имя")
    def input_name(self, name):
        self.send_keys(NAME, name)
    
    @allure.step("Вводим фамилию")
    def input_lastname(self, lastname):
        self.send_keys(LASTNAME, lastname)

    @allure.step("Ввод адреса")
    def input_address(self, address):
        self.send_keys(ADDRESS, address)

    @allure.step("Выбор метро")
    def choose_metro(self, station):
        self.click(METRO)
        self.wait_visibility(metro_station(station))
        self.click(metro_station(station))
    
    @allure.step("Ввод телефона")
    def input_phone(self, phone):
        self.send_keys(PHONE, phone)

    @allure.step("Нажать далее")
    def click_next_button(self):
        self.click(NEXT_BUTTON)

    @allure.step("Заполение формы заказа")
    def full_order (self, name, lastname, address, station, phone):
        self.input_name(name)
        self.input_lastname(lastname)
        self.input_address(address)
        self.choose_metro(station)
        self.input_phone(phone)

    @allure.step("Нажать на лого Самокат")
    def click_scooter(self):
        self.click(SCOOTER_BUTTON)

    @allure.step("Нажать на лого Яндекс")
    def click_yandex(self):
        self.click(YANDEX_BUTTON)
     
    @allure.step("Переход в Дзен через логотип Яндекс")
    def open_dzen_by_yandex_logo(self):
        self.click_yandex()
        self.switch_to_new_window()


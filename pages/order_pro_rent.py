from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.locators_pro_rent import *
import allure


class OrderProRentPageScooter(BasePage):

    @allure.step("Открыть страницу")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждем загрузки страницы")
    def wait_for_rent_page(self):
        self.wait_visibility(DATE)

    @allure.step("Выбрать дату")
    def choose_date(self, date):
        self.click(DATE)
        date = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{date}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(date))
        self.click(date)

    @allure.step("Выбрать период")
    def choose_last(self, last):
        self.click(LAST)
        last = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{last}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(last))
        self.click(last)
    
    @allure.step("Выбрать цвет")
    def choose_color(self, color):
        if color == 'black':
            self.click(COLOR_BLACK)
        elif color == 'grey':
            self.click(COLOR_GREY)
 
    @allure.step("Ввод комментария")
    def input_comment(self,comment):
        self.send_keys(COMMENT, comment)
    
    @allure.step("Нажать заказать")
    def click_order_button(self):
        self.click(ORDER_BUTTON)

    @allure.step("Заполение формы заказа")
    def fill_rent(self, date, last, color, comment):
        self.choose_date(date)
        self.choose_last(last)
        self.choose_color(color)
        self.input_comment(comment)

    @allure.step("Нажать Да")
    def click_order_yes(self):
        self.click(ORDER_YES)

    @allure.step("Подождать загрузки страницы")
    def wait_for_success(self):
        self.wait_visibility(SUCCESS_WINDOW)

    
    @allure.step("Проверить отображение окна")
    def is_success_message_displayed(self):
        return self.is_displayed(SUCCESS_MESSAGE)

    
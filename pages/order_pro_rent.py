from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure


class OrderProRentPageScooter(BasePage):
    DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    LAST = [By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"]
    COLOR_BLACK = [By.ID, "black"]
    COLOR_GREY = [By.ID, "grey"]
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    
    ORDER_BUTTON = [By.XPATH, "//button[text()='Заказать']"]
    
    ORDER_YES = [By.XPATH, "//button[text()='Да']"]
    ORDER_NO = [By.XPATH, "//button[text()='Нет']"]

    SUCCESS_WINDOW = [By.XPATH, "//div[contains(@class, 'Order_Modal')]"]
    SUCCESS_MESSAGE = [By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(text(), 'Заказ оформлен')]"]
    STATUS_BUTTON = [By.XPATH, "//button[text()='Посмотреть статус']"]

    @allure.step("Открыть страницу")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждем загрузки страницы")
    def wait_for_rent_page(self):
        self.wait_visibility(self.DATE)

    @allure.step("Выбрать дату")
    def choose_date(self, date):
        self.click(self.DATE)
        date = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{date}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(date))
        self.click(date)

    @allure.step("Выбрать период")
    def choose_last(self, last):
        self.click(self.LAST)
        last = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{last}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(last))
        self.click(last)
    
    @allure.step("Выбрать цвет")
    def choose_color(self, color):
        if color == 'black':
            self.click(self.COLOR_BLACK)
        elif color == 'grey':
            self.click(self.COLOR_GREY)
 
    @allure.step("Ввод комментария")
    def input_comment(self,comment):
        self.send_keys(self.COMMENT, comment)
    
    @allure.step("Нажать заказать")
    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    @allure.step("Заполение формы заказа")
    def fill_rent(self, date, last, color, comment):
        self.choose_date(date)
        self.choose_last(last)
        self.choose_color(color)
        self.input_comment(comment)

    @allure.step("Нажать Да")
    def click_order_yes(self):
        self.click(self.ORDER_YES)

    @allure.step("Подождать загрузки страницы")
    def wait_for_success(self):
        self.wait_visibility(self.SUCCESS_WINDOW)

    @allure.step("Получить текст с экрана")
    def get_success_text(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    
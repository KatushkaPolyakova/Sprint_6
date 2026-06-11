from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class OrderProRentPageScooter:
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
        self.driver = driver

    @allure.step("Ждем загрузки страницы")
    def wait_for_rent_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.DATE))

    @allure.step("Выбрать дату")
    def choose_date(self, date):
        self.driver.find_element(*self.DATE).click()
        date = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{date}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(date))
        self.driver.find_element(*date).click()

    @allure.step("Выбрать период")
    def choose_last(self, last):
        self.driver.find_element(*self.LAST).click()
        last = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{last}']")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(last))
        self.driver.find_element(*last).click()
    
    @allure.step("Выбрать цвет")
    def choose_color(self, color):
        if color == 'black':
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == 'grey':
            self.driver.find_element(*self.COLOR_GREY).click()
 
    @allure.step("Ввод коментарция")
    def input_comment(self,comment):
        self.driver.find_element(*self.COMMENT).send_keys(comment)
    
    @allure.step("Нажать заказать")
    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    @allure.step("Заполение формы заказа")
    def fill_rent(self, date, last, color, comment):
        self.choose_date(date)
        self.choose_last(last)
        self.choose_color(color)
        self.input_comment(comment)

    @allure.step("Нажать Да")
    def click_order_yes(self):
        self.driver.find_element(*self.ORDER_YES).click()


    @allure.step("Подождать загрузки страницы")
    def wait_for_success(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.SUCCESS_WINDOW))

    @allure.step("Получить текст с экрана")
    def get_success_text(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    
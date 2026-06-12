from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure

class HomePageScooter(BasePage):

    COOKIE_ACCEPT_BUTTON = [By.ID, 'rcc-confirm-button']
    

    QUESTIONS = [        
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
        ]
    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]

    ORDER_BUTTON_HEADER = [By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"]
    ORDER_BUTTON_BOTTOM = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"]

    @allure.step('Открываем страницу')
    def __init__(self, driver):
        super().__init__(driver)
 
    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.click(self.COOKIE_ACCEPT_BUTTON)

    @allure.step("Ждем прогрузки станицы")
    def wait_for_load_home_page(self):
        self.wait_visibility(self.QUESTIONS)

    @allure.step("Нажать на вопрос")    
    def click_question(self, index):
        self.scroll_to_element(self.QUESTIONS[index])
        self.click(self.QUESTIONS[index])
        
    @allure.step("Ждем появления ответа")
    def wait_for_answer(self,index):
        self.wait_visibility(self.ANSWERS[index])

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        return self.get_answer_text(self.ANSWERS[index])

    @allure.step("Нажать кнопку заказать")
    def click_order_button(self,order_button):
        self.scroll_to_element(order_button)
        self.click(order_button)
        

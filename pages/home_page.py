from pages.base_page import BasePage
from locators.locators_home import *
import allure


class HomePageScooter(BasePage):

    @allure.step('Открываем страницу')
    def __init__(self, driver):
        super().__init__(driver)
 
    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.click(COOKIE_ACCEPT_BUTTON)

    @allure.step("Ждем прогрузки станицы")
    def wait_for_load_home_page(self):
        self.wait_visibility(QUESTIONS[0])

    @allure.step("Нажать на вопрос")    
    def click_question(self, index):
        self.scroll_to_element(QUESTIONS[index])
        self.click(QUESTIONS[index])
        
    @allure.step("Ждем появления ответа")
    def wait_for_answer(self,index):
        self.wait_visibility(ANSWERS[index])

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        return self.get_text(ANSWERS[index])

    @allure.step("Нажать кнопку заказать")
    def click_order_button(self,order_button):
        self.scroll_to_element(order_button)
        self.click(order_button)


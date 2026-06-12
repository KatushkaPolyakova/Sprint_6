
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
from data.constants import BASE_URL, DZEN_URL
from locators.locators_home import ORDER_BUTTON_HEADER
import allure


class TestNavigation:
    @allure.title("Клик на лого скутера, переход на домашнюю станицу")    
    def test_click_scooter_logo_open_home_page(self, driver):
            home_page = HomePageScooter(driver)
            order_page = OrderPageScooter(driver)

            home_page.open(BASE_URL)

            home_page.accept_cookies()
            home_page.wait_for_load_home_page()
            home_page.click_order_button(ORDER_BUTTON_HEADER)

            order_page.wait_for_order_page()
            order_page.click_scooter()     
            assert order_page.get_current_url() == BASE_URL
        

    @allure.title("Клик на лого яндекса, переход на станицу дзена")
    def test_click_yandex_logo_open_dzen(self, driver):
            home_page = HomePageScooter(driver)
            order_page = OrderPageScooter(driver)

            home_page.open(BASE_URL)

            home_page.accept_cookies()
            home_page.wait_for_load_home_page()
            home_page.click_order_button(ORDER_BUTTON_HEADER)

            order_page.wait_for_order_page()
            order_page.open_dzen_by_yandex_logo()
            
            assert DZEN_URL in order_page.current_url()
        

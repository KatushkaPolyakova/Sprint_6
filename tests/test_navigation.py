import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter


class TestNavigation:
        
    def test_click_scooter_logo_open_home_page(self, driver):
            driver.get('https://qa-scooter.education-services.ru/')
            home_page = HomePageScooter(driver)
        
            home_page.accept_cookies()
            home_page.wait_for_load_home_page()
            home_page.click_order_button(HomePageScooter.ORDER_BUTTON_HEADER)
            rent_page = OrderPageScooter(driver)
            rent_page.wait_for_order_page()
            rent_page.click_scooter()     
            assert driver.current_url == 'https://qa-scooter.education-services.ru/'
        
    def test_click_yandex_logo_open_dzen(self, driver):
            driver.get('https://qa-scooter.education-services.ru/')
            home_page = HomePageScooter(driver)
            
            home_page.accept_cookies()
            home_page.wait_for_load_home_page()
            home_page.click_order_button(HomePageScooter.ORDER_BUTTON_HEADER)
            rent_page = OrderPageScooter(driver)
            rent_page.wait_for_order_page()
            rent_page.click_yandex()
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)     
            driver.switch_to.window(driver.window_handles[1])
            assert 'dzen.ru' in driver.current_url
        

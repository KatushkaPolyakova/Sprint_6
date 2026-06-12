import pytest
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
from pages.order_pro_rent import OrderProRentPageScooter
from data.data_order import ORDER_DATA_1, ORDER_DATA_2
from locators.locators_home import ORDER_BUTTON_BOTTOM, ORDER_BUTTON_HEADER
from data.constants import BASE_URL
import allure


class TestOrder:
    @allure.title("Успешное оформление заказа через верх и нижнюю кнопки")
    @pytest.mark.parametrize(
        'order_button, name, lastname, address, station, phone, date, last, color, comment',
        [
             (ORDER_BUTTON_HEADER, *ORDER_DATA_1),
             (ORDER_BUTTON_BOTTOM, *ORDER_DATA_2)
        ]
    )

    def test_order_is_sucсess(self, driver, order_button, name, lastname, address, station, phone, date, last, color, comment):
    
        home_page = HomePageScooter (driver)
        order_page = OrderPageScooter(driver)
        rent_page = OrderProRentPageScooter(driver)

        home_page.open(BASE_URL)

        home_page.accept_cookies()
        home_page.wait_for_load_home_page()
        home_page.click_order_button(order_button)

        order_page.wait_for_order_page()
        order_page.full_order(name, lastname, address, station, phone)
        order_page.click_next_button()

        rent_page.wait_for_rent_page()
        rent_page.fill_rent(date, last, color, comment)
        rent_page.click_order_button()

        rent_page.click_order_yes()
        rent_page.wait_for_success()
    
        assert 'Заказ оформлен' in rent_page.get_success_text()
    

        


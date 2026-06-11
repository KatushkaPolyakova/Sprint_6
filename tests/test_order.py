import pytest
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
from pages.order_pro_rent import OrderProRentPageScooter


class TestOrder:

    @pytest.mark.parametrize(
        'order_button, name, lastname, address, station, phone, date, last, color, comment',
        [
            (
                HomePageScooter.ORDER_BUTTON_HEADER,
                'Олег', 'Зайцев', 'Бухвостова, 12',
                'Сокольники', '89111111111',
                '29', 'четверо суток', 'black', 'скорее скорее'
            ),
            (
                HomePageScooter.ORDER_BUTTON_BOTTOM,
                'Рома', 'Киров', 'Площадь Восстания, 1',
                'Охотный ряд', '89222222222',
                '1', 'сутки', 'grey', 'надо еще вчера'
            )
        ]
    )


    def test_order_is_sucсess(self, driver, order_button, name, lastname, address, station, phone, date, last, color, comment):
        
        driver.get('https://qa-scooter.education-services.ru/')

        home_page = HomePageScooter (driver)
        order_page = OrderPageScooter(driver)
        rent_page = OrderProRentPageScooter(driver)

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
    

        


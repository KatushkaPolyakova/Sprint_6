import pytest
from pages.home_page import HomePageScooter
from data.data_FAQ import FAQ_DATA



class TestFAQ:

    @pytest.mark.parametrize('index, expected_text', 
                            FAQ_DATA
                            )
    
    def test_click_question_get_correct_answer(self, driver, index, expected_text):
        driver.get('https://qa-scooter.education-services.ru/')

        home_page= HomePageScooter(driver)
        home_page.accept_cookies()
        home_page.wait_for_load_home_page()
        home_page.click_question(index)
        home_page.wait_for_answer(index)

        assert home_page.get_answer_text(index) == expected_text

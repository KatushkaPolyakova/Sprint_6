from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_base import *



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

    def switch_to_new_window(self):
        self.wait_new_window()
        self.driver.swith_to.window(self.driver.window_handles[1])
        
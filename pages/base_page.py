from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

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
        
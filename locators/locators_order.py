from selenium.webdriver.common.by import By


NAME = (By.XPATH, "//input[@placeholder='* Имя']")
LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

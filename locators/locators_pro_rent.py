from selenium.webdriver.common.by import By


DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
LAST = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
COLOR_BLACK = (By.ID, "black")
COLOR_GREY = (By.ID, "grey")
COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    
ORDER_YES = (By.XPATH, "//button[text()='Да']")
ORDER_NO = (By.XPATH, "//button[text()='Нет']")

SUCCESS_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(text(), 'Заказ оформлен')]")
STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

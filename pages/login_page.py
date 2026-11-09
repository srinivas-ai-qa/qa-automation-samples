from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()
        return self

    def error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text

    def is_inventory_visible(self):
        return "inventory" in self.driver.current_url

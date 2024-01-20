from selenium.webdriver.common.by import By


class AboutPage:

    def __init__(self, driver):
        self.driver = driver
        self.header_about = "header.my-4"

    def get_header_about(self):
        header_about = self.driver.find_elements(By.CSS_SELECTOR, self.header_about)
        return header_about


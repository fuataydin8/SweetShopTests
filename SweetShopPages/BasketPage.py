from selenium.webdriver.common.by import By


class BasketPage:

    def __init__(self, driver):
        self.driver = driver
        self.items = 'ul[id="basketItems"] .lh-condensed div h6'
        self.about = 'a[href="/about"]'

    def get_basket_items(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, self.items)
        items_text = []

        for i in range(0, len(items)):
            items_text.append(items[i].get_attribute("innerHTML"))

        return items_text

    def open_about(self):
        about = self.driver.find_element(By.CSS_SELECTOR, self.about)
        about.click()
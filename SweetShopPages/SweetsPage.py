from selenium.webdriver.common.by import By


class SweetsPage:

    def __init__(self, driver):
        self.url = "https://sweetshop.netlify.app/sweets"
        self.driver = driver
        self.images = ".container .row .col-lg-3 .card img"
        self.buttons = ".container .row .col-lg-3 .card .card-footer a"
        self.titles = ".container .row .col-lg-3 .card .card-body h4"
        self.basket = 'a[href="/basket"]'
        self.about = 'a[href="/about"]'

    def open_page(self):
        self.driver.get(self.url)

    def iterate_images(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, self.images)
        nat_widths = []

        for i in range(0, len(images)):
            nat_widths.append(images[i].get_attribute("naturalWidth"))

        return nat_widths

    def add_to_basket(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, self.buttons)
        exp_titles = self.driver.find_elements(By.CSS_SELECTOR, self.titles)
        exp_titles_text = []

        for i in range(0, len(buttons)):
            buttons[i].click()
            exp_titles_text.append(exp_titles[i].get_attribute("innerHTML"))

        return exp_titles_text

    def open_basket(self):
        basket = self.driver.find_element(By.CSS_SELECTOR, self.basket)
        basket.click()

    def open_about(self):
        about = self.driver.find_element(By.CSS_SELECTOR, self.about)
        about.click()

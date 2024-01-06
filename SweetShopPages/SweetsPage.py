from selenium.webdriver.common.by import By


class SweetsPage:

    def __init__(self, driver):
        self.url = "https://sweetshop.netlify.app/sweets"
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def iterate_images(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".container .row .col-lg-3 .card img")
        nat_widths = []

        for i in range(0, len(elements)):
            nat_widths.append(elements[i].get_attribute("naturalWidth"))

        return nat_widths

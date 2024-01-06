import os

from selenium import webdriver

from SweetShopPages.SweetsPage import SweetsPage


class TestSweetShopImage:

    def test_image_sweet_shop(self):
        os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
        driver = driver = webdriver.Firefox()

        sweets_page = SweetsPage(driver)
        sweets_page.open_page()
        nat_widths = sweets_page.iterate_images()

        assert '0' not in nat_widths

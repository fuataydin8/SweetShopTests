import os
from collections import Counter

from selenium import webdriver

from SweetShopPages.SweetsPage import SweetsPage

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()
sweets_page = SweetsPage(driver)

# Errors found until now:
# 1 - When added to the basket, the product 'Whistles' changes its name to 'Sweet Whistles'
# just inside the basket for no apparent reason.
# 2 - The image for the product 'Wham Bars' is not loading correctly.


class TestSweetShop:

    def test_image_sweet_shop(self):
        sweets_page.open_page()
        nat_widths = sweets_page.iterate_images()

        assert '0' not in nat_widths

    def test_add_to_basket_sweet_shop(self):
        sweets_page.open_page()
        exp_basket = sweets_page.add_to_basket()

        sweets_page.open_basket()
        basket = sweets_page.get_basket_items()

        assert exp_basket == basket

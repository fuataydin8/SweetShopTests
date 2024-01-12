import os
from collections import Counter

from selenium import webdriver

from SweetShopPages.SweetsPage import SweetsPage

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()
sweets_page = SweetsPage(driver)

# Errors found until now:
# 1 - When added to the basket, several names of products change inside the basket, this
# probably would confuse some users when buying sweets in the store if it was a real store.
# 2 - The image for the product 'Wham Bars' is not loading correctly.
# 3 - It's currently not possible to enter the "about" page from the basket page because
# there's no element with href="about" in it


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

    def test_open_about_from_basket(self):
        sweets_page.open_page()
        sweets_page.open_basket()
        sweets_page.open_about()

        title_about = sweets_page.get_header_about()
        assert len(title_about) != 0

    def test_open_about(self):
        sweets_page.open_page()
        sweets_page.open_about()

        header_about = sweets_page.get_header_about()
        assert len(header_about) != 0


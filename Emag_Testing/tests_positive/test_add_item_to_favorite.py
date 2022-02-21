import time
from selenium.webdriver.common.by import By
from Emag_Testing.pages.main_page import Emag


def test_add_items_to_favorite(page_browser):
    new_shopping = Emag(page_browser)
    new_shopping.open_emag_page()
    item_list = new_shopping.ITEMS_LIST
    for x in item_list:
        new_shopping.search_bar_search(x)
        new_shopping.click_add_to_favorite_button()
        new_shopping.clear_text()
    time.sleep(5)

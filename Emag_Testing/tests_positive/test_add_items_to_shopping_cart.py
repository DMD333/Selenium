import time
from selenium.webdriver.common.by import By
from Emag_Testing.pages.main_page import Emag
from selenium.webdriver.common.keys import Keys


def test_add_3_items_to_shopping_cart(page_browser):
    """
    - This function lunch the Chrome browser and open Emag main page;
    - Loop through a list of items by searching them in the page and adding to the shopping cart
    """
    new_shopping = Emag(page_browser)
    new_shopping.open_emag_page()
    items = new_shopping.ITEMS_LIST
    for x in items:
        new_shopping.search_bar_search(x)
        new_shopping.click_add_to_cart_button()
        time.sleep(2)

        """
        - Aici verifica daca apare un anume text dintr-o fereastra noua deschisa si inchide fereastra
        - Nu functioneaza corect, imi zice ca selectorul nu are nici un atribut
        """
        if page_browser.select_by_visible_text("Produsul a fost adaugat in cos"):
            new_shopping.close_frame_window()
        else:
            print("This type of issue hasn't been handled. Check the cause")

        new_shopping.clear_text()
        time.sleep(2)

    time.sleep(120)

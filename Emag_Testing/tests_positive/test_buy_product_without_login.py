import time
from selenium.webdriver.common.by import By
from Emag_Testing.pages.main_page import Emag


def test_buy_product_without_login(page_browser):
    buy_product = Emag(page_browser)
    page_browser.maximize_window()
    buy_product.open_emag_page()
    buy_product.search_bar_search(buy_product.ITEMS_LIST[0])
    buy_product.scroll_to_element_2(page_browser)

    page_browser.find_element(By.XPATH, '//*[@id="card_grid"]/div[34]/div/div/div[4]/div[2]/form/button').click()
    # buy_product.click_shopping_cart_icon()
    time.sleep(5)
from Emag_Testing.pages.main_page import Emag
import time


def test_login(page_browser):
    """
    This function will open Emag page in the chrome browser and create an account
    """

    new_browser = Emag(page_browser)
    new_browser.open_emag_page()
    new_browser.click_login_icon()
    page_browser.implicitly_wait(100)
    new_browser.insert_email_address(new_browser.EMAIL)
    new_browser.click_continue_login_button()
    new_browser.insert_full_name(new_browser.NAME)
    new_browser.insert_password(new_browser.PASSWORD)
    new_browser.password_confirmation(new_browser.PASSWORD)
    new_browser.click_checkbox()
    time.sleep(1)
    new_browser.click_continue_registration_button()
    time.sleep(5)
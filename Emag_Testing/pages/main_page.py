from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Emag:
    # -------------------------------    URL    ---------------------------------
    URL = "https://www.emag.ro/"
    # ----------------------------    LOCATORS    -------------------------------
    SEARCH_BAR = (By.ID, "searchboxTrigger")
    SHOPPING_CART_BUTTON = (By.ID, "my_cart")
    FAVORITE_ITEM_BUTTON = (By.ID, "my_wishlist")
    EMAG_NAV_BUTTON = (By.CSS_SELECTOR, ".navbar-brand>img")
    LOGIN_ICON = (By.CSS_SELECTOR, "#my_account>i")

    # -----------------------------     ITEMS     --------------------------------
    ITEMS_LIST = ["Iphone 12 Pro Max", "Samsung Galaxy S21 Ultra", "Huawei P40 Pro"]

    ADD_FIRST_TO_CART_BUTTON = (By.CSS_SELECTOR, "div:first-child>div>div>div>div>form>button[type='submit']")
    ADD_TO_FAVORITE = (By.CSS_SELECTOR, "#card_grid >div:first-child button.add-to-favorites.btn > i")

    ITEM_INTO_SPECIFIC_LOCATION = (By.CSS_SELECTOR, 'div:nth-child(34) > div > div > div.card-v2-info')

    # ----------------------     CREDENTIAL / REGISTER    ------------------------
    EMAIL = "ppalomin@mailcuk.com"
    NAME = "Mega Buyer"
    PASSWORD = "Ab3d4r_"

    MESSAGE_INSERT_EMAIL = (By.CLASS_NAME, "required")
    INSERT_EMAIL_LOGIN = (By.ID, "user_login_email")

    INSERT_FULL_NAME = (By.ID, "user_register_full_name")
    INSERT_PASSWORD = (By.ID, "user_register_password_first")
    PASSWORD_CONFIRMATION = (By.ID, "user_register_password_second")

    CHECKBOX_1 = (By.CSS_SELECTOR, "label[class='required']")
    CHECKBOX_2 = (By.CSS_SELECTOR, "label[for='user_register_subscribe_newsletter']")

    CONTINUE_LOGIN_BUTTON = (By.ID, "user_login_continue")
    CONTINUE_USER_REGISTRATION_BUTTON = (By.ID, "user_register_continue")

    CLOSE_FRAME_WINDOW = (By.CLASS_NAME, "close.gtm_6046yfqs")

    # ============================================================================

    def __init__(self, browser):
        self.browser = browser

    def open_emag_page(self):
        self.browser.get(self.URL)

    def search_bar_search(self, item_name):
        self.browser.find_element(*self.SEARCH_BAR).send_keys(item_name, Keys.ENTER)

    def click_shopping_cart_icon(self):
        self.browser.find_element(*self.SHOPPING_CART_BUTTON).click()

    def click_favorite_icon(self):
        self.browser.find_element(*self.FAVORITE_ITEM_BUTTON).click()

    def click_emag_logo(self):
        self.browser.find_element(*self.EMAG_NAV_BUTTON).click()

    def click_login_icon(self):
        self.browser.find_element(*self.LOGIN_ICON).click()

    def insert_email_address(self, email):
        self.browser.find_element(*self.INSERT_EMAIL_LOGIN).send_keys(email)

    def click_continue_login_button(self):
        self.browser.find_element(*self.CONTINUE_LOGIN_BUTTON).click()

    def insert_full_name(self, name):
        self.browser.find_element(*self.INSERT_FULL_NAME).send_keys(name)

    def insert_password(self, password):
        self.browser.find_element(*self.INSERT_PASSWORD).send_keys(password)

    def password_confirmation(self, password):
        self.browser.find_element(*self.PASSWORD_CONFIRMATION).send_keys(password)

    def click_checkbox(self):
        self.browser.find_element(*self.CHECKBOX_1).click()
        self.browser.find_element(*self.CHECKBOX_2).click()

    def click_continue_registration_button(self):
        self.browser.find_element(*self.CONTINUE_USER_REGISTRATION_BUTTON).click()

    def click_add_to_cart_button(self):
        self.browser.find_element(*self.ADD_FIRST_TO_CART_BUTTON).click()

    def click_add_to_favorite_button(self):
        self.browser.find_element(*self.ADD_TO_FAVORITE).click()

    def clear_text(self):
        self.browser.find_element(*self.SEARCH_BAR).clear()

    def close_frame_window(self):
        self.browser.find_element(*self.CLOSE_FRAME_WINDOW).click()

    def is_name_displayed(self):
        a = self.browser.find_element_by_name("Introdu adresa de email")
        return a.is_dyplayed()

    def scroll_to_element(self, driver):
        element = driver.find_element(*self.ITEM_INTO_SPECIFIC_LOCATION)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("window.scrollBy(0, 600)", "(0, 200)")


    """
    - This another example of a METHOD, who to scroll to element
    """
    def scroll_to_element_2(self, driver):
        element = driver.find_element(*self.ITEM_INTO_SPECIFIC_LOCATION)
        action = ActionChains(driver)
        action.move_to_element(element).perform()
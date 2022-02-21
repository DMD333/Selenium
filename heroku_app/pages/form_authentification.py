import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


class FormAuthentification():
    # URL
    URL = ("https://the-internet.herokuapp.com/login")

    # CREDENTIALS
    USER_NAME_SELECTOR = (By.CSS_SELECTOR, 'input#username')
    PASSWORD_SELECTOR = (By.CSS_SELECTOR, 'input#password')

    # Log In Button / Log Out Button
    LOG_IN_BUTTON = (By.CSS_SELECTOR, 'button.radius')
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "a[class='button secondary radius']")

    # Successful Log In Message - Selector
    LOG_IN_MESSAGE= (By.ID, 'flash')
    LOG_OUT_MESSAGE = (By.ID, 'flash')

    def __init__(self, browser):

        self.browser = browser

    def openPage(self):
        return self.browser.get(self.URL)

    def inserttUserName(self, username):
        self.browser.find_element(*self.USER_NAME_SELECTOR).send_keys(username)

    def insertPassword(self, password):
        self.browser.find_element(*self.PASSWORD_SELECTOR).send_keys(password)

    def clickLogInButton(self):
        self.browser.find_element(*self.LOG_IN_BUTTON).click()

    def clickLogOutButton(self):
        self.browser.find_element(*self.LOG_OUT_BUTTON).click()

    def ifLogInSuccessMessage(self):
        return self.browser.find_element(*self.LOG_IN_MESSAGE).text

    def ifLogOutSuccessfulMessage(self):
        return self.browser.find_element(*self.LOG_OUT_MESSAGE).text

    def verifyNegativePassword(self, user_name, password, message_invalid):
        i = len(password)-1
        while(i > 0):
            self.browser.find_element(*self.USER_NAME_SELECTOR).send_keys(user_name)
            self.browser.find_element(*self.PASSWORD_SELECTOR).send_keys(password[0:i])
            time.sleep(.2)
            self.browser.find_element(*self.LOG_IN_BUTTON).click()

            if message_invalid in self.browser.find_element(*self.LOG_IN_MESSAGE).text:
                i -= 1






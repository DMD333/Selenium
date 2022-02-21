import datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from heroku_app.pages.form_authentification import FormAuthentification

USER_NAME = ('tomsmith')
PASSWORD = ('SuperSecretPassword!')

# Successful Log In Message
LOG_IN_MESSAGE = ("You logged into a secure area!")
LOG_OUT_MESSAGE = ("You logged out of the secure area!")

INVALID_PASSWORD = ("Your password is invalid!")


def testLogIn(browser):
    webpage = FormAuthentification(browser)
    webpage.openPage()
    # webpage.inserttUserName(USER_NAME)
    # webpage.insertPassword(PASSWORD)
    # webpage.clickLogInButton()
    # assert LOG_IN_SUCCESS_MESSAGE in webpage.ifLogInSuccessMessage()
    # webpage.clickLogOutButton()
    # assert LOG_OUT_SUCCESS_MESSAGE in webpage.ifLogOutSuccessfulMessage()
    webpage.verifyNegativePassword(USER_NAME, PASSWORD, INVALID_PASSWORD)

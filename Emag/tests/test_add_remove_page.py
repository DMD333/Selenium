import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from test_curs.pages.add_remove_elements_page import AddRemoveElementsPage

def test_add_button_functionality(browser):

    add_remove_page = AddRemoveElementsPage(browser)

    # Load page
    add_remove_page.loadPage()

    add_remove_page.clickAddElementButton()

    add_remove_page.clickDeleteButton()

    # assert add_remove_page.isDeleteElementButtonDisplayes() == 1

    for i in range(9):
        add_remove_page.clickAddElementButton()

    # assert add_remove_page.getNumberOfDeleteButton() == 10


def test_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.loadPage()
    assert add_remove_page.getTitleText() == 'Add/Remove Elements'
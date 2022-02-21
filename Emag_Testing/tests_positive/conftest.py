import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def page_browser():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield driver

    driver.quit()

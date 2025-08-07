import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver =  webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_in_page_title(driver):
    driver.get('https://www.google.com')
    assert "Google" in driver.title

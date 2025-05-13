import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_login_ui():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("user", "pass")
    assert login_page.is_login_successful()
    driver.quit()

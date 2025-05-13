import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://example.com"

@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# --- utils/browser_utils.py ---
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import platform
import os

def get_browser_driver(browser_name="chrome", headless=False):
    """Returns a Selenium WebDriver instance based on the browser name and OS."""
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        options.add_argument('--start-maximized')
        service = ChromeService(executable_path=ChromeDriverManager(path="drivers/chrome").install())
        return webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        service = FirefoxService(executable_path=GeckoDriverManager(path="drivers/firefox").install())
        return webdriver.Firefox(service=service, options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument('--headless')
        service = EdgeService(executable_path=EdgeChromiumDriverManager(path="drivers/edge").install())
        return webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

def quit_driver(driver):
    """Closes and quits the browser driver safely."""
    try:
        driver.quit()
    except Exception as e:
        print(f"Error quitting driver: {e}")

# Example usage:
# driver = get_browser_driver("chrome", headless=True)
# driver.get("https://example.com")
# quit_driver(driver)

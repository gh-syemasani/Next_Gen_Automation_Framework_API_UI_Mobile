from appium import webdriver
import json

def get_mobile_driver():
    with open("config/capabilities.json") as f:
        caps = json.load(f)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    return driver
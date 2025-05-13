from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

@given('the user is on the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('they enter valid credentials')
def step_enter_credentials(context):
    context.login_page.login("user", "pass")

@then('they should see the dashboard')
def step_verify_login(context):
    assert context.login_page.is_login_successful()
    context.driver.quit()

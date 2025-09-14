from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.HomePage import homepage
from features.Pages.LoginPage import loginpage


@given('user should be on login page')
def launchApp(context):
    context.driver.get("http://localhost:100")
    context.login_page = loginpage(context.driver)


@when('user enter the valid credentials')
def login(context):
    context.login_page.login("admin", 'admin')


@when('user enter the invalid credentials')
def invalid_login(context):
    context.login_page.login("admin12", 'admin12')


@then('user should navigate to home page')
def verifyHome(context):
    context.home_page = homepage(context.driver)
    context.home_page.verifyHome()


@then('user should see the error message')
def verifyErrorMsg(context):
    context.login_page.verifyErrorMsg()



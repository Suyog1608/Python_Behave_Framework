from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.Pages.HomePage import homepage
from features.Pages.LeadPage import leadpage
from features.Pages.LoginPage import loginpage


@when('user click on new lead')
def clickNewLead(context):
    # Browser launch is already written in login.feature
    context.home_page = homepage(context.driver)
    context.home_page.click_NewLead()


@when('user fills the mandatory fields and click save')
def createNewLead(context):
    context.lead_page = leadpage(context.driver)
    context.lead_page.create_lead("Suyog", "Infor")


@then('lead should be created successfully')
def verify_lead(context):
    pass

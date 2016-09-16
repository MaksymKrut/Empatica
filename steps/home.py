'''
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
'''


from behave import *


@given("I am on the home page")
def step_impl(context):
    context.browser.get("https://www.empatica.com/")
    pass


@when("I navigate to Order Embrace watch page")
def step_impl(context):
    context.browser.find_element_by_id("storeDropdown").click()
    context.browser.find_element_by_css_selector("#main-navbar > div > ul > li.dropdown.open > ul > *:nth-child(1) > a").click()
    context.browser.implicitly_wait(5)
    pass


@when("I navigate to Order E4 wristband page")
def step_impl(context):
    context.browser.find_element_by_id("storeDropdown").click()
    context.browser.find_element_by_css_selector("#main-navbar > div > ul > li.dropdown.open > ul > *:nth-child(2) > a").click()
    context.browser.implicitly_wait(5)
    pass



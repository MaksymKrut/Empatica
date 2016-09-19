"""
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
"""
from common import *


@given("I am on the home page")
def step_impl(context):
    url = get_value_from_ini_file("config", "Base", "home url")
    context.browser.get(url)


@when("I click on {element} element")
def step_impl(context, element):
    locator = get_value_from_ini_file("locators", "Header", element)
    context.browser.find_element_by_css_selector(locator).click()


@then("I should see {text} text")
def step_impl(context, text):
    page = context.browser.page_source
    plain = page.encode('ascii', 'ignore')
    if text not in plain:
        print ("\n\nTest" + plain + "\n\nTest")
        raise Exception('Was not found!')


# @then("the url should contain {text}")
# def step_impl(context, text):
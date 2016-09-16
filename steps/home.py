'''
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
'''


from behave import *
import time
from selenium import webdriver


@given("I am on the home page")
def step_impl(context):
    context.browser.get("https://www.empatica.com/")
    context.browser.find_element_by_id("storeDropdown")
    context.browser.find_element_by_id("storeDropdown")


def step_impl(context):



def step_impl(context):




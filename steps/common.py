"""
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
"""
import configparser

from behave import *
import time


@when("I wait for {number} seconds")
def step_impl(number):
    assert isinstance(number, int)
    time.sleep(number)


def get_value_from_ini_file(file_name, section_header, key):
    config = configparser.ConfigParser()
    config.read("support/" + file_name + ".ini")
    value = config[section_header][key]
    return value


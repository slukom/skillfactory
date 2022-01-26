#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py


import time


def test_search_example(selenium):
    selenium.get('https://www.google.com/')
    time.sleep(3)

    search_input = selenium.find_element_by_name('q')
    search_input.clear()
    search_input.send_keys('first test')
    time.sleep(3)

    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()
    time.sleep(3)

    selenium.save_screenshot('module24/result.png')

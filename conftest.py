# Для дополнительной настройки работы браузера (размер окна, режим отображения и так далее), рекомендуется
# использовать фикстуры. Их стоит вставлять в файл conftest.py, который находится в корневой директории тестового
# проекта.

import uuid
import pytest
import time
from selenium import webdriver

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = '/home/slukom/PycharmProjects/geckodriver'
    firefox_options.add_argument('-foreground')  # возможность запуска в фоновом или реальном режиме.
    # В нашем случае выбран последний. Для фонового укажите ‘-background’.
    firefox_options.set_preference('browser.anchor_color', '#FF0000')  # выбор цвета подложки браузера
    return firefox_options

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/home/slukom/PycharmProjects/chromedriver' # путь к exe браузера (включая сам исполняемый файл)
    #chrome_options.add_extension('/path/to/extension.crx')  # включение дополнений браузера
    chrome_options.add_argument('--kiosk')
    #chrome_options.set_headless(True)  # режим запуска без пользовательского интерфейса, так называемый headless-режимом («без головы»)
    return chrome_options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here


def test_petfriends(web_browser):
   # Open PetFriends base page:
   web_browser.get("https://petfriends1.herokuapp.com/")

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   # click on the new user button
   btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
   btn_newuser.click()

   # click existing user button
   btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
   btn_exist_acc.click()

   # add email
   field_email = web_browser.find_element_by_id("email")
   field_email.clear()
   field_email.send_keys("<your_email>")

   # add password
   field_pass = web_browser.find_element_by_id("pass")
   field_pass.clear()
   field_pass.send_keys("<your_pass>")

   # click submit button
   btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
   btn_submit.click()

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   assert web_browser.current_url == 'https://petfriends1.herokuapp.com/all_pets',"login error"
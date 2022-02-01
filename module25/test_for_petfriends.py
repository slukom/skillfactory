# Задание 25.3.1.
# Написать тест, который проверяет, что на странице http://petfriends1.herokuapp.com/my_pets со списком питомцев пользователя:
# * Присутствуют все питомцы.
# * Хотя бы у половины питомцев есть фото.
# * У всех питомцев есть имя, возраст и порода.
# * У всех питомцев разные имена.
# * В списке нет повторяющихся питомцев. (Сложное задание).

# Задание 25.5.1.
# * В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).
# * В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.

import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password, valid_login


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('../drivers/chromedriver')
    # устанавливаем неявное ожидание
    pytest.driver.implicitly_wait(10)
    # Увеличиваем размер окна браузера на весь экран
    pytest.driver.maximize_window()

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    # Сохраняем скриншот страницы "Мои питомцы"
    pytest.driver.save_screenshot('my_pets.png')

    yield

    pytest.driver.quit()


@pytest.fixture()
def get_pets_num():  # возвращаем число питомцев из блока статистики пользователя
    acc_info = pytest.driver.find_elements_by_css_selector('div.task3 > div.left')[0].text
    #  Извлекаем из найденного текста информацию про количество питомцев
    pets_num = acc_info.split()[2]

    # Проверяем, что число питомцев положительное или равно 0
    assert int(pets_num) >= 0

    return int(pets_num)


@pytest.fixture()
def get_pets_info():  # получить значения имен, возрастов, пород из таблицы с питомцами
    #names, ages, types = [], [], []
    # находим все имена питомцев
    names = pytest.driver.find_elements_by_css_selector('tbody > tr > td:nth-of-type(1)')
    # находим все возраста питомцев
    ages = pytest.driver.find_elements_by_css_selector('tbody > tr > td:nth-of-type(2)')
    # находим все породы питомцев
    types = pytest.driver.find_elements_by_css_selector('tbody > tr > td:nth-of-type(3)')

    # преобразуем найденные элементы в текстовый список имен
    text_names = [names[i].text for i in range(len(names))]
    # преобразуем найденные элементы в текстовый список возрастов
    text_ages = [ages[i].text for i in range(len(ages))]
    # преобразуем найденные элементы в текстовый список пород
    text_types = [types[i].text for i in range(len(types))]

    return text_names, text_ages, text_types


# test1
def test_all_my_pets_are_in_table(get_pets_num):  # проверяем, что присутствуют все питомцы
    table_rows = []
    try:
        # Находим и запоминаем количество строк в таблице с питомцами
        # table_rows = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table tr')
        table_rows = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#all_my_pets > table tr'))
        )
    except TimeoutException:
        print("Не удалось загрузить элементы на странице")

    finally:
        # Проверяем, что количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя
        assert get_pets_num == len(table_rows) - 1


# test2
def test_half_of_pets_have_photo(get_pets_num):  # проверяем, что хотя бы у половины питомцев есть фото
    photos = []
    try:
        # Находим все картинки в таблице
        # photos = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table img')
        photos = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#all_my_pets > table img'))
        )
    except TimeoutException:
        print("Не удалось загрузить элементы на странице")

    finally:
        # Проверяем, что у половины есть фото
        photo_count = 0
        for i in range(len(photos)):
            if photos[i].get_attribute('src') != '':
                photo_count += 1
        assert photo_count >= get_pets_num / 2


# test3
def test_all_pets_have_name_age_type(get_pets_info):  # проверяем, что у всех питомцев есть имя, возраст и порода
    names, ages, types = get_pets_info
    # проверяем, что у всех питомцев есть имя, возраст и порода
    for i in range(len(names)):
        # print('\nNAME: ', names[i])
        assert names[i] != ''
        # print('AGE: ', ages[i])
        assert ages[i] != ''
        # print('TYPE: ', types[i])
        assert types[i] != ''

# test4
def test_all_pets_have_diff_name(get_pets_num, get_pets_info):  # проверяем, что у всех питомцев разные имена
    names, ages, types = get_pets_info
    # создаем словарь питомцев
    pets = {}
    # заполняем словарь добавляя
    for i in range(len(names)):
        pets[names[i]] = (ages[i], types[i])

    assert get_pets_num == len(pets)


# test5
def test_all_pets_are_unique(get_pets_info):  # проверяем, что в списке нет повторяющихся питомцев (питомцы, у которых одинаковое имя, порода и возраст.)
    names, ages, types = get_pets_info
    flag = True  # отвечает за проверку найденных повторяющихся питомцев (True - все питомцы уникальны, False - есть повторяющиеся)

    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            if names[i] == names[j] and ages[i] == ages[j] and types[i] == types[j]:
                flag = False  # нашли одну повторяющуюся пару питомцев
                break  # выходим из вложенного цикла
        if not flag:
            break  # нашли одну повторяющуюся пару питомцев, выходим из первого цикла

    assert flag == True

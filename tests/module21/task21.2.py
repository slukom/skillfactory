import functools
from decorators import do_twice

def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

@my_decorator  # синтаксический сахар
def my_first_decorator():
    print("Это мой первый декоратор!")


my_first_decorator()
print()

@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")

@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))

test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = test_twice("single")
print(decorated_value)

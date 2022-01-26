# Напишите функцию, которая определяет, можно ли составить треугольник из трёх отрезков,
# длины которых передаются в функцию.
# Например, вызов функции is_triangle(3, 4, 5) возвращает True, а вызов is_triangle(1, 4, 5) возвращает False.
# Напишите параметризованный тест на эту функцию, используя фикстуру @pytest.mark.parametrize, который рассматривает
# все возможные варианты параметров:
#
# Негативные тесты:
# * Отрицательные длины отрезков;
# * Длины, равные 0;
# * Положительные длины отрезков, из которых невозможно составить треугольник.
#
# Позитивные тесты:
# * Положительные длины, из которых можно составить треугольник.

import pytest

testdata = [
    (1, 1, 1, True),
    (3, 4, 5, True),
]

def is_triangle(a, b, c):
    return True if (a + b) > c > 0 and (b + c) > a > 0 and (a + c) > b > 0 else False


@pytest.mark.parametrize("a", [-5, 0, 1])
@pytest.mark.parametrize("b", [-5, 0, 4])
@pytest.mark.parametrize("c", [-5, 0, 5])
def test_negative(a, b, c):
    print("a: {0}, b: {1}, c: {2}".format(a, b, c))
    assert not is_triangle(a, b, c)


@pytest.mark.parametrize("a, b, c, expected", testdata)
def test_positive(a, b, c, expected):
    result = is_triangle(a, b, c)
    print("a: {0}, b: {1}, c: {2}".format(a, b, c))
    assert result == expected

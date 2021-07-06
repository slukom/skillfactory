# Напишите функцию count, которая возвращает количество вхождений элемента в массив

def find(array, element): # Линейный поиск
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    c = 0
    for i, a in enumerate(array):
        if a == element:
            c += 1
    return c

array = list(map(int, input().split()))
print(array)
element = int(input())

print(find(array, element))

print(count(array, element))
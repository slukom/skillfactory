# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается 
# у пользователя любое число. В качестве задания повышенного уровня сложности можете выполнить проверку соответствия 
# указанному в условии ввода данных.
# Далее программа работает по след. алгоритму
# 1. Преобразование введенной последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
# или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией 

def sort(array):
    for i in range(len(array)):
        idx_max = i
        for j in range(i, len(array)):
            if array[j] < array[idx_max]:
                idx_max = j
        if i != idx_max:
            array[i], array[idx_max] = array[idx_max], array[i]
    return array


def binary_search(array, element, left, right):
    if element < array[0]:
        #print("Введенное число самое маленькое")
        return False
    if left > right:  # если левая граница превысила правую,
        return right  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if (array[middle] == element) or (array[middle-1] < element <= array[middle]):  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


array = list(map(int, input('Введите целые числа через пробел:\n').split()))
print('Преобразуем в список:', array)
print('Отсортируем список:  ', sort(array))
print('Индексы элементов:   ', [i for i in range(len(array))])
element = int(input('Введите любое число: '))
result = binary_search(array, element, 0, len(array) - 1)

if not result and isinstance(result, bool):
    print("Введенное число минимальное")
elif result == -1:
    print("Введенное число совпадает с нулевым элементом списка")
elif result == len(array) - 1:
    print("Введенное число больше последнего (%d - го) элемента списка" % (len(array) - 1))
else:
    print("Номер позиции элемента, который меньше введенного числа:", result)

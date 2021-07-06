# Сортировка пузырьком

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print('Было')
print(array)

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print('Стало после сортировки выбором')
print(array)
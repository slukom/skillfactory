# Быстрая сортировка. Алгоритм выполняется рекурсивно следующим образом:
# 1. Выбирается ведущий элемент
# 2. Две части массива сортируются только на основе этого ведущего элемента.
# 3. Происходит последовательный обмен значениями элементов. Сначала происходит поиск слева направо до первого элемента,
# который превосходит по своему значению ведущий элемент. Затем массив просматривается справа налево в поисках элемента,
# который меньше ведущего. Когда такие элементы найдены, происходит их обмен.
# 4. Таким образом, в левой части массива имеются элементы только меньше ведущего, а в правой — только больше.
# 5. Функция рекурсивно применяется к получившимся частям массива, если их размеры превосходят один элемент.

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print('Было')
print(array)
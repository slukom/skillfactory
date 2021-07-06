# Найдите количество цифр в записи числа 100! (факториал от 100)

def factorial(num):
    if num == 0:
        return 1
    p = 1
    for i in range(num):
        p = p * (i + 1)
    return p

def digits_number(num):
    count = 1
    while num > 10:
        count += 1
        num = num/10
    return count

number = int(input('Введите положительное целое число: '))

print(factorial(number), digits_number(factorial(number)))
while True:
    try:
        n = int(input('Сколько билетов Вы хотите купить? Введите целое число: '))
        if n <= 0 or n > 5000:
            raise ValueError("Неверное число билетов, может быть от 1 до 5000")
    except ValueError:
        print('Некорректное число, попробуйте еще раз\n')
    else:
        break

sum = 0

for i in range(n):
    print()
    while True:
        try:
            age = int(input(f'Введите возраст {i+1}-го посетителя: '))
            if age > 100 or age <= 0:
                raise ValueError("Некорректный возраст, посетитель может быть от 1 до 100 лет")
        except ValueError:
            print("Ошибка в возрасте, попробуйте ввести еще раз")
        else:
            break

    if 18 <= age < 25:
        sum += 990
    if age >= 25:
        sum += 1390

if n > 3:
    sum = 0.9 * sum
    print(f'\nОбщая стоимость за {n} билетов с учетом скидки составляет: {sum} руб.')
else:
    print(f'\nОбщая стоимость за {n} билетов составляет: {sum} руб.')
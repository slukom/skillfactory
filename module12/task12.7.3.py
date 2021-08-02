per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input('Какую сумму в руб. Вы хотите положить под проценты? Введите целое число: '))

deposit = [round(per_cent['ТКБ'] / 100 * money), round(per_cent['СКБ'] / 100 * money),
           round(per_cent['ВТБ'] / 100 * money), round(per_cent['СБЕР'] / 100 * money)]

print(f'Список процентов: {deposit}')
print(f'Максимальная сумма, которую Вы можете заработать - {max(deposit)}')

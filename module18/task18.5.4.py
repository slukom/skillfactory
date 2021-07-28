# Напишите программу, которая будет записывать и кэшировать номера ваших друзей. Программа должна уметь воспринимать
# несколько команд: записать номер, показать номер друга в консоли при вводе имени или же удалить номер друга по имени.
# Кэширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль (с помощью
# функций input() и print()).

import redis
import json

dict = {}

red = redis.Redis(
    host='localhost',
    port='6379',
    password=''
)

while True:
    action = input('Введите действие (write, read, delete, exit): ')
    if action == 'write':
        name = input('Введите имя друга: ')
        tel = input('Введите его номер телефона: ')
        red.set(name, tel)
        print()

    if action == 'read':
        name = input('Введите имя друга, чтобы найти его номер: ')
        tel = red.get(name)
        if tel:
            print('Номер телефона %s: %s \n' % (name, str(tel)))
        else:
            print('Такой друг не был добавлен\n')

    if action == 'delete':
        name = input('Введите имя друга, чтобы удалить: ')
        tel = red.get(name)
        if tel:
            red.delete(name)
            print('Друг %s удален\n' % (name))
        else:
            print('Такой друг не был добавлен\n')

    if action == 'exit':
        break

    if action not in ['write', 'read', 'delete', 'exit']:
        print('Введено некорректное действие, попробуйте снова!\n')
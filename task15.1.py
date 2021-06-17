# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
# читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.

import os.path


def find_most_common_word(word_list):
    found_word = False  # считаем что в списке слов не было ни одного слова длинее 3-х символов
    repeatability = {}

    for word in word_list:
        if len(word) > 3:
            found_word = True  # нашли слово длинее 3-х символов
            if word in repeatability:  # если слово встречалось увеличим его счетчик
                repeatability[word] += 1
            else:  # иначе слово добавляем в словарь
                repeatability[word] = 1

    if found_word:
        max_value = max(repeatability.values())
        if max_value == 1: # проверяем чтобы максимальное число повторений было более 1 раза
            found_word = False
        else:
            for key, value in repeatability.items():
                if value == max_value:
                    print('Слово с максимальным числом повторений и размером более трех символов: %s (число '
                          'повторений %s)' % (key, value))

    return found_word


def find_longest_eng_word(word_list):
    eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    eng_word_list = []

    for word in word_list:
        is_eng_word = True
        for char in word:
            if char not in eng_alphabet:
                is_eng_word = False
        if is_eng_word:
            eng_word_list.append(word)

    if len(eng_word_list) == 0:
        return False
    else:
        max_length = 0

        for word in eng_word_list:
            if max_length < len(word):
                max_length = len(word)

        for word in eng_word_list:
            if len(word) == max_length:
                print('Самое длинное анг.слово: %s (длина слова %d)' % (word, len(word)))
    return True


while True:
    file_name = input("Введите имя файла либо 'exit' для выхода из программы: ")
    if file_name == "exit":
        break
    if os.path.isfile(file_name):
        with open(file_name, encoding='utf8') as f:
            file_content = f.read()
            # print("Содержимое файла:", file_content, sep="\n")
            print("Содержимое файла: \n%s" % file_content)
            file_content = file_content.lower()
            print()

            separators = ['.', ',', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '&', '/', '|']

            for separator in separators:
                file_content = file_content.replace(separator, ' ')

            words = file_content.split()

            first_found_word = find_most_common_word(words)
            if not first_found_word:
                print('В файле %s нет слов длинее 3-х символов либо всего по 1-му разу встречаются слова из более '
                      '3-х символов' % file_name)

            second_found_word = find_longest_eng_word(words)
            if not second_found_word:
                print('В файле %s нет английских слов' % file_name)
        break

    else:
        print("Такого файла нет в этом каталоге. Пожалуйста, повторите ввод еще раз")

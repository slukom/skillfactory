# Написать простой тест, который проверяет JSON на правильность полей. То есть проверяет, что каждый объект в JSON:
# 1. Содержит все перечисленные в требованиях поля.
# 2. Не имеет других полей.
# 3. Все поля имеют именно тот тип, который указан в требованиях:
# + int — целое число;
# + string — произвольная строка;
# + string (url) — это строка с url. В рамках этого задания проверяем, что url начинается c http:\\ или https:\\;
# + string (itemBuyEvent или itemViewEvent) — строка, в которой могут быть только эти конкретные два значения и никакие
# другие;
# + bool — булево значение, то есть True или False.
# Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными, и причину, почему они ошибочные.

import json
import os.path


def validate_dict(data):  # передаем словарь
    sample = {'timestamp': int, 'referer': str, 'location': str, 'remoteHost': str,
              'partyId': str, 'sessionId': str, 'pageViewId': str, 'eventType': str,
              'item_id': str, 'item_price': int, 'item_url': str, 'basket_price': str,
              'detectedDuplicate': bool, 'detectedCorruption': bool, 'firstInSession': bool,
              'userAgentName': str}

    if isinstance(data, dict):  # проверяем, что в функцию передан словарь
        for sample_key, sample_data in sample.items():  # проверка 1: Содержит все перечисленные в требованиях поля
            if sample_key not in data.keys():
                print('Fail: объект не соотвествует требованию "1. Содержит все перечисленные в требованиях поля", '
                      'т.к. обязательное поле ', sample_key,  ' со значением ', sample_data, ' отсутствует у переданного объекта')
                print(json.dumps(data, indent=4), '\n')
                return False  # объект не соотвествует первому требованию, завершаем проверку

        for data_key, data_value in data.items(): # проверка 2: Не имеет других полей; и 3: Все поля имеют указанный тип
            if data_key not in sample.keys():  # есть несоотвествующее поле во входящих данных
                print('Fail: объект не соотвествует требованию "2. Не имеет других полей" т.к. поле ', data_key,
                      ' со значением ', data_value, ' не соответствуют требуемому формату')
                print(json.dumps(data, indent=4), '\n')
                return False  # объект не соотвествует первому требованию, завершаем проверку
            else:

                if not isinstance(data_value, (sample[data_key])):  # тип значения не соответсвует ожидаемому
                    print('Fail: объект не соотвествует требованию "3. Все поля имеют указанный тип", т.к. значение ',
                          data_value, 'в поле ', data_key,' не соответсвует типу ', sample[data_key])
                    print(json.dumps(data, indent=4), '\n')
                    return False

                if data_key == 'referer' or data_key == 'location' or data_key == 'item_url':  # уточняем типы полей
                    if data_value.find('http://', 0, len('http://')) == -1 and data_value.find('https://', 0, len('https://')) == -1:  # 3 поля должны быть типа string (url)
                        print('Fail: объект не соотвествует требованию "3. Все поля имеют указанный тип", т.к. у одного'
                              ' из полей referer, location или data_key указана некорректная ссылка: ', data_value)
                        print(json.dumps(data, indent=4), '\n')
                        return False

                if data_key == 'eventType' and (data_value != 'itemBuyEvent' and data_value != 'itemViewEvent'):
                    print('Fail: объект не соотвествует требованию "3. Все поля имеют указанный тип", т.к. значение поля'
                          ' eventType = ', data_value, ', а должно быть itemBuyEvent или itemViewEvent')
                    print(json.dumps(data, indent=4), '\n')
                    return False


        return True  # все условия выполнены

    return False  # если был передан не словарь


def check_json(data):  # передаем содержимое json файла
    if isinstance(data, list):  # проверяем, что в функцию передан список объектов
        passed = True  # считаем, что все поля у всех объектов соответсвуют требованиям
        for item in data:
            if not validate_dict(item):  # нашелся несоответсвующий объект
                passed = False

        if passed:  # если все поля у всех объектов соответсвуют требованиям
            print('Pass')
    else:
        print('Был передан не список объектов в формате json')


while True:
    file_name = input("Введите имя JSON файла либо 'exit' для выхода из программы: ")
    if file_name == "exit":
        break
    if file_name.find('.json', len(file_name) - len('.json'), len(file_name)) > -1:  # проверяем, что файл формата JSON
        if os.path.isfile(file_name):
            with open(file_name, encoding='utf8') as f:
                templates = json.load(f)

                check_json(templates)

                break
        else:
            print("Такого файла нет в этом каталоге. Пожалуйста, повторите ввод еще раз\n")
    else:
        print('Был выбран не JSON файл, попробуйте еще раз\n')

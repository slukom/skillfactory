import json
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder

filename = 'log.txt'
f = open(filename, 'w')
f.close()


def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""

    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        # print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        f = open(filename, 'a')
        f.write(f"\n\nФункция{func.__name__!r} отправила запрос: {value[0].request.method!r} {value[0].request.url!r}")
        f.write(
            f"\nЗаголовок запроса: {value[0].request.headers!r}\nПараметры пути запроса: {value[0].request.path_url!r}")
        f.write(f"\nПараметры строки запроса: {value[0].request.url!r}\nТело запроса: {value[0].request.body!r}")
        f.write(f"\nКод ответа: {value[1]!r}\nТело ответа: {value[2]!r}")
        return value

    return wrapper_debug


class PetFriends:
    """API библиотека к веб-приложению Pet Friends"""

    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    @debug
    def get_api_key(self, email: str, password: str) -> json:
        """Метод отправляет запрос на получение ключа API и возвращает статус запроса и результат в формате JSON
        с уникальным ключаом пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except:
            result = res.text

        print('\nres.request.url = ', res.request)
        return res, status, result

    @debug
    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Метод отправляет запрос на получение списка питомцев, соответствующих фильтру, и возвращает статус
        запроса и результат в формате JSON. На данный момент фильтр может иметь либо пустое значение - получить
        список всех питомцев, либо 'my_pets' - получить список собственных питомцев"""

        headers = {
            'auth_key': auth_key['key']
        }

        filter = {
            'filter': filter
        }

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return res, status, result

    @debug
    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Метод отправляет запрос на создание питомца и возвращает статус запроса и результат в формате JSON"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }
        )

        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return res, status, result

    @debug
    def create_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет запрос на создание питомца без фото и возвращает статус запроса и результат в формате
        JSON"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        headers = {
            'auth_key': auth_key['key']
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return res, status, result

    @debug
    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет запрос на удаление питомца по указанному ID  и возвращает статус запроса
        и результат в формате JSON с текстом уведомления об успешном удалении."""

        headers = {
            'auth_key': auth_key['key']
        }

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return res, status, result

    @debug
    def update_pet(self, auth_key: json, pet_id: str, new_name: str, new_animal_type: str, new_age: str) -> json:
        """Метод отправлеяет запрос на обновелние питомца по ID и возвращает статус запроса
        и результат в формате JSON об обновленном питомце."""
        new_data = {
            'name': new_name,
            'animal_type': new_animal_type,
            'age': new_age
        }

        headers = {
            'auth_key': auth_key['key']
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=new_data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return res, status, result

    @debug
    def add_pet_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на добавление фото питомца и возвращает статус запроса и результат в формате JSON"""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }
        )

        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return res, status, result


    def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return res, status, result

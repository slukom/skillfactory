import requests
import json # импортируем необходимую библиотеку

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print("1) content of requests.get("
      "'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html'):\n", r.content)
print('status_code: ', r.status_code)  # узнаем статус полученного ответа


r = requests.get('https://baconipsum.com/api/?type=meat-and-filler') # попробуем поймать json ответ
print("\n2) json response from r = requests.get('https://baconipsum.com/api/?type=meat-and-filler'):\n", r.content)

texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print('type of convert response: ', type(texts))  # проверяем тип сконвертированных данных

print('\nconvert content to json:')
for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50])


r = requests.get('https://api.github.com')
print("\n3) content of requests.get('https://api.github.com'):\n", r.content)

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print('type of content: ', type(d))
print("d['following_url']: ", d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
print('full content:', d)


r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
print("\n4) content of requests.post('https://httpbin.org/post', data = {'key':'value'}):\n", r.content) # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет


data = {'key': 'value'}
r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print("\n5) content of requests.post('https://httpbin.org/post', json=json.dumps(data)):\n", r.content)
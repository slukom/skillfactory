# Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис
# https://baconipsum.com/api/). Выведите первый из сгенерированных текстов.

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)
print(texts[0])
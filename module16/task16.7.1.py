# Откройте сайт «Дом питомца»(http://130.193.37.179/app/pets) и на основе имеющихся в нем данных создайте конструктор 
# класса Cat со следующими параметрами: имя, пол, возраст.
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов, с одинаковыми 
# параметрами, но с разными значениями.

from cat import Cat

cat1 = Cat('Барон', 'male', 2)
cat2 = Cat('Сэм', 'male', 2)

cat1.getCat()
cat2.getCat()
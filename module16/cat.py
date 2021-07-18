#Задание 16.7.1.
# Откройте сайт «Дом питомца» http://130.193.37.179/app/pets и на основе имеющихся в нем данных создайте конструктор
# класса Cat со следующими параметрами: имя, пол, возраст.
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов, с одинаковыми
# параметрами, но с разными значениями.

class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getCat(self):
        print('Имя кота: %s; пол: %s; возраст: %s' % (self.name, self.sex, self.age))

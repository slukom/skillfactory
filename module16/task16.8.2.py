# Добавьте класс — круг (class Circle), который принимает в качестве аргументов свой радиус.
# Вычислите площадь круга (вспомните формулу).

from rectangle import Rectangle, Square, Circle

radius = int(input("Введите число, которое будет радиусом: "))
circle = Circle(radius)
print ("площадь круга: ", circle.get_area_circle())
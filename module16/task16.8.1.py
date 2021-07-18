from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print("площадь 1-го прямоугольника: ", rect_1.get_area())
print("площадь 2-го прямоугольника: ", rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("площадь 1-го квадрата: ", square_1.get_area_square())
print("площадь 2-го квадрата: ", square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square): # Если экземпляр класса figure является квадратом, то вызываем метод get_area_square
        print(figure.get_area_square())
    else: # В противном случае — обрабатываем данные для прямоугольника методом get_area
        print(figure.get_area())
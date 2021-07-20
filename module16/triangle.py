class Triangle:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def get_rignt_angle_coordinates(self):
        print("x = %s, y = %s" % (self.x, self.y))

    def get_triangle_area(self):
        return self.a * self.b / 2

    def get_legs(self):
        print('a = %s, b = %s' % (self.a, self.b))

    def hypotenuse(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def get_attributes(self):
        attributes = "Triangle(" + str(self.x) + ", " + str(self.y) + ", " + str(self.a) + ", " + str(self.b) + ")"
        return attributes
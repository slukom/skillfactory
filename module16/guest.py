class Guest:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_status(self):
        return 'Статус: ' + self.status
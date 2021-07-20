class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_client_info(self):
        info = 'Клиент "' + self.name + '". Баланс: ' + str(self.balance) + ' руб.'
        return info
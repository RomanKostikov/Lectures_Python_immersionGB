# Инкапсуляция
class User:
    def __init__(self, name, phone, password):
        self.__name__ = name
        self._phone = phone
        self.__password = password


u1 = User('One', '123-45-67', 'qwerty')
print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password =}')

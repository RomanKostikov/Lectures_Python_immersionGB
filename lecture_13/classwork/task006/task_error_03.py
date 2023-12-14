# 4. Создание собственных исключений
# Методы __init__ и __str__ в классах своих
# исключений
# Чтобы исключение давало подробную информацию об ошибке, будем передавать
# ему проблемную переменную. Класс User доработаем в строках подъёма ошибок.
from classwork.task006.task_error_01 import UserNameError, UserAgeError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User('Яков', '-12')
# Благодаря наследованию переданные в исключение переменные могут выводится
# в тексте ошибки.
# raise UserNameError(name)
# error.UserNameError: Яков
# Уже лучше. Но без пары дандер методов в классах ошибок пока не идеально

# ● Deleter
# Помимо “геттера” и “сеттера” можно создать “делейтер”. Он выполняется при
# вызове команды del для свойства. Один из возможных вариантов использования
# “делейтера” - заменять значение на какое-то по умолчанию или помечать элемент
# скрытым вместо удаления.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')

    @age.deleter
    def age(self):
        self._age = 0


user = User('Стивен', 'Спилберг')
user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло много лет. Изобретена технология перерождения.')
del user.age
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# Создание “делейтера” аналогично “сеттеру”. Также используется декоратор с
# именем свойства, но после точки пишем deleter. Внутри метода прописываются
# действия для удаления.

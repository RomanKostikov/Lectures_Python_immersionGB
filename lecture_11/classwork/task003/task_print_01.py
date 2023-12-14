# 3. Представления экземпляра
# При работе с классами, а точнее с их экземплярами бывает необходимо вывести их
# содержимое в консоль. С этим отлично справляется функция print, но есть одно но.
# Попробуем “запринтить” класс из примера выше.
class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


user = User('Спенглер')
print(user)
# В результат получили строку вида <__main__.User object at 0x000001C1B4FA6B60>
# Число в конце — адрес объекта в оперативной памяти. Он может быть разным для
# разных ПК и даже при разных запусках программы. Но пользы от этой информации
# немного. Для получения читаемого описания необходимо переопределить как
# минимум один из дандер методов: __str__ или __repr__.

# 5. Сравнение экземпляров класса
# Неизменяемые экземпляры, хеширование
# дандер __hash__
# Как вы помните ключом dict и элементами set и frozenset могут быть только
# неизменяемые типы данных. А для проверки на неизменяемость используется
# функция hash(). Она должна возвращать целое число в 4 или 8 байт в зависимости
# от разрядности интерпретатора Python. И это число должно быть неизменным на
# всём протяжении работы программы.
# Попробуем сложить наши треугольники из примера выше в множество не изменяя
# код.
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    # def __eq__(self, other):
    #     first = sorted((self.a, self.b, self.c))
    #     second = sorted((other.a, other.b, other.c))
    #     return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()


triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(triangle_set)
print(', '.join(f'{hash(item)}' for item in triangle_set))
# Получаем ошибку TypeError: unhashable type: 'Triangle' ведь дандер __hash__ у нас
# не реализован. Прежде чем приступать к написанию кода попробуем
# закомментировать метод проверки на равенство и запустит код снова.
# Работает! Экземпляры треугольника стали хэшируемыми. Правило следующее.
# ● нет __eq__, нет __hash__ - неизменяемый объект. Python сам реализует оба
# дандера
# ● есть __eq__, нет __hash__ - изменяемый объект. Python устанавливает
# __hash__ = None
# ● есть __eq__, есть __hash__ - неизменяемый объект реализованный
# разработчиком
# ● нет __eq__, есть __hash__ - запрещённая комбинация! Разработчик допустил
# ошибку
# Если вы хотите явно отключить поддержку хэширования, в определение класса
# добавляется строка __hash__ = None
# class Triangle:
# __hash__ = None

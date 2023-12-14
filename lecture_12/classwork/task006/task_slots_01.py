# 6. Экономим память
# Мы уже несколько раз сталкивались с дандер словарём __dict__. Его
# предназначение — хранить атрибуты и их значения у каждого объекта Python.
# Хранитель атрибутов __dict__
# Рассмотрим уже знакомый по прошлой лекции класс Triangle и выведем на печать
# содержимое __dict__ у экземпляра и у класса.
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'

    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'

    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second

    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        return hash((self._a, self._b, self._c))


triangle = Triangle(3, 4, 5)
print(triangle)
print(triangle.__dict__)
print(Triangle.__dict__)

# Как видите экземпляр хранить лишь три свойства, определённые внутри метода
# инициализации. За всем остальным он обращается к своему классу.
# Что касается класса, его словарь имена и адреса дандеров, методов и даже пустой
# дандер __doc__, ведь мы не сделали строку документации.
# При редкой необходимости можно обращаться к ключам словаря для получения
# или изменения значений.

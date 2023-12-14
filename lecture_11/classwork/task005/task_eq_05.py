# 5. Сравнение экземпляров класса
# Простейшая реализация хэша
# При желании реализовать собственный метод __hash__ рекомендуется сделать все
# свойства класса неизменяемыми. Внутри дандер метода возвращается результат
# работы функции hash(). На вход функция получает кортеж из всех свойств класса.
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


triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(triangle_set)
print(', '.join(f'{hash(item)}' for item in triangle_set))
# Свойства класса получили символ подчёркивания в начале имени. Сообщаем
# коллегам по коду, что они защищённые и не должны изменяться.
# 🔥 Важно! Как вы помните это договорённость, которую можно обойти.
# Философия Python надеется на разумного человека, который понимает что
# делать, а что нет.
# Сам дандер __hash__ возвращает результат вычисления хэша для кортежа из трёх
# элементов — длин сторон.

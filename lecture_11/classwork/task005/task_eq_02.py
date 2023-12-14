# 5. Сравнение экземпляров класса
# А теперь напишем свою проверку на идентичность. Допустим возможность
# переворачивания треугольника перед сравнением. Например треугольники со
# сторонами 3, 4, 5 и 4, 3, 5 будем считать равными.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        """"True if id(self) == id(other) else False"""
        return self is other


one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
print(one == two)
print(one == three)
# Переменные one и two равны, т.к. ссылаются на один и тот же объект в памяти. А вот
# треугольники one и three считаются разными хоть и имеют одинаковые длины
# сторон. Дело в том, что Python по умолчанию добавляет метод __eq__ следующего
# вида.
# def __eq__(self, other):
# return self is other
# Как вы помните is сравнивает адреса объектов в памяти. Следовательно проверка
# по умолчанию это: True if id(self) == id(other) else False.

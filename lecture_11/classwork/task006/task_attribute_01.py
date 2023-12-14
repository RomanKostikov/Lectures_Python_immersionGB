# 6. Обработка атрибутов
# Python имеет четыре дандер метода, которые позволяют контролировать
# обращения к атрибутом экземпляра. Разберём их на простом примере класса
# вектор.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


a = Vector(2, 4)

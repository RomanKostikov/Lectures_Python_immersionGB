# 6. Обработка атрибутов
# Присвоение атрибуту значения, __setattr__
# Дандер __setattr__ срабатывает каждый раз, когда в коде есть операция
# присвоения. Слева от знака равно экземпляр со свойством - key, справа значение -
# value.

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

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)


a = Vector(2, 4)
# print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')
# a.z = 73  # AttributeError: У нас вектор на плоскости, а не в пространстве
a.x = 3
print(f'{a = }')
# Дандер __setattr__ запрещает присваивать значение свойству . Как и в случае с
# __getattribute__ важная последняя строка. Она позволяет избежать рекурсии и
# присвоить значение свойству, которое мы не обработали ранее.

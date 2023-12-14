# 6. Обработка атрибутов
# Удаление атрибута, __delattr__
# При попытке удалить атрибут командой del можно использовать дандер __delattr__
# для изменения логики.
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

    def __getattr__(self, item):
        return None

    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            return object.__delattr__(self, item)


a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(f'{a = }, {a.s = }')
# В нашем классе при попытке удалить икс или игрек, значение не удаляется. Вместо
# этого свойству присваивается ноль.
# Обратите внимание на свойство s. Мы смогли присвоить ему значение 73. Дандер
# __setattr__ контролирует только имя z. При удалении свойства z сработала ветка
# else и свойство было удалено. Однако мы не получили ошибки, обращаясь к
# несуществующему свойству, сработал дандер __getattr__.

# 6. Обработка атрибутов
# Обращение к несуществующему атрибуту,
# __getattr__
# Если свойство отсутствует, в первую очередь вызывается дандер __getattribute__. В
# случае возврата им ошибки AttributeError вызывается метод __getattr__. Он также
# может поднять ошибку. А может как-то иначе обработать запрос.
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


a = Vector(2, 4)
print(a.z)  # None
print(f'{a = }')
# Мы попросили возврат None для любого свойства, которое не удалось найти. Метод
# возвращает None и для свойства z, перехватывая исключение.

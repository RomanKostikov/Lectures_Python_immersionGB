# 6. Обработка атрибутов
# Получение значения атрибута,
# __getattribute__
# Дандер __getattribute__ вызывается при любой попытке обращения к атрибутам
# экземпляра.
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
    

a = Vector(2, 4)
print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')
# В параметр item попадает имя атрибута, к которому пытаются обратиться в виде str.
# Мы прописали проверку имён и если это третья координата z, вызываем ошибку
# AttributeError.
# 🔥 Важно! Строка return object.__getattribute__(self, item) является
# обязательной. Без неё может возникнуть ошибка переполнения стека.

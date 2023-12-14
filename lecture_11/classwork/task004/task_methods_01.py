# 4. Математика и логика в классах
# Сложение через __add__
# Создадим класс вектор и научим вектора складываться.
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
b = Vector(3, 7)
c = a + b
print(f'{a = }\t{b = }\t{c = }')
# Помимо уже привычных методов __init__ и __repr__ определили метод __add__. В
# предпоследней строке пытаемся сложить вектора. Без метода __add__ получили бы
# ошибку вида: TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'.
# В самом методе используем два параметра — self для обращения к элементам
# экземпляра и other для обращения к элементам другого объекта, стоящего справа
# от знака плюс. Получив значения x, y для нового вектора метод возвращает его -
# новый экземпляр класса Vector.

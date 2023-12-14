# 4. Пара полезных структур данных
# Как и в случае с неизменяемыми датами, экземпляры namedtuple также неизменны.
# Но если надо внести правку в какое-то поле, встроенный метод _replace создаст
# копию, заменив только указанные значения.
from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)

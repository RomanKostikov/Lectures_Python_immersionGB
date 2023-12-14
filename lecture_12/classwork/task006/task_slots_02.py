# 6. Экономим память
# Экономия памяти, __slots__
# При создании класса можно явно указать перечень имён свойств, которые в нём
# будут использоваться.
# class Triangle:
# __slots__ = ('_a', '_b', '_c')
# def __init__(self, a, b, c):
# ...
# Подобная запись говорит о том, что теперь у нас лишь три свойства. Python не
# позволит добавить новые.
# А при попытке обратится к словарю экземпляра получим ошибку AttributeError:
# 'Triangle' object has no attribute '__dict__'. Did you mean: '__dir__'?
# Коротко о том, что даёт замена изменяемого __dict__ на неизменяемый __slots__?
# 1. Обеспечивает немедленное обнаружение ошибок из-за неправильного
# написания атрибутов. Допускаются только имена атрибутов, указанные в
# __slots__
# 2. Помогает создавать неизменяемые объекты, в которых дескрипторы
# управляют доступом к закрытым атрибутам, хранящимся в __slots__
# 3. Экономит память. В 64-битной сборке Linux экземпляр с двумя атрибутами
# занимает 48 байт со __slots__ и 152 байт без него. Экономия памяти имеет
# значение только тогда, когда будет создано большое количество
# экземпляров.
# 4. Улучшает скорость. По данным на Python 3.10 на процессоре Apple M1 чтение
# переменных экземпляра выполняется на 35% быстрее со __slots__().
# 5. Блокирует такие инструменты как functools.cached_property(), которым для
# правильной работы требуется экземплярный словарь.
from math import sqrt


class Triangle:
    __slots__ = ('_a', '_b', '_c')

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
# print(triangle.__dict__)
print(Triangle.__dict__)

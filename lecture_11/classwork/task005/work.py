# Сравнение экземпляров
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def __str__(self):
        return f'MyClass(a= {self.a}, b={self.b}, c={self.c})'

    def __eq__(self, other):
        return (sum((self.a, self.b)) - self.c) == (sum((other.a, other.b)) - other.c)


x = MyClass(42, 2)
y = MyClass(73, 3)
print(f'({x == y})')    # 0==0 т. к. идет двойное сложение, а потом вычиатние этих чисел

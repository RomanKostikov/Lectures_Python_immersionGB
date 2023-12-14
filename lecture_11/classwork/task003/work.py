# Представление экземпляра
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'

    def __repr__(self):
        return str(self.a) + str(self.b) + str(self.c)  # неправильно так как склееваем строчки, а не возвращаем экземпляр

# Что не верно?

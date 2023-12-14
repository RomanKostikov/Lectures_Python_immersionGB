# Строка документации
class MyClass:
    A = 42
    """About class"""

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b

    def method(self):
        """Documentation"""
        self.__doc__ = None


help(MyClass)

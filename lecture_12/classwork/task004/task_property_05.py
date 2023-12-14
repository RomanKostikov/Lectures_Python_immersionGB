# Антипаттерн геттера, сеттера, делейтера
# Представленный ниже код является кодам ради кода и не имеет смысла в языке
# Python. Избегайте подобного. И да, код работает верно. Просто он не делает ничего
# нового.
class BadPattern:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

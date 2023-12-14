# В зависимости от решаемой задачи некоторые пункты могут отсутствовать.
# Учебный пример модуля ниже:
# Файл base_math.py
"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
"""
_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1


def add(*args):
    res = _START_SUM
    for item in args:
        res += item
    return res


def sub(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res -= item
    return res


def mul(*args):
    res = _START_MULT
    for item in args:
        res *= item
    return res


def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res /= item
    return res


if __name__ == '__main__':
    print(f'{add(2, 4) = }')
    print(f'{add(2, 4, 6, 8) = }')
    print(f'{sub(10, 2) = }')
    print(f'{mul(2, 2, 2, 2, 2) = }')
    print(f'{div(-100, 5, -2) = }')

# Как вы заметили, в файле нет классов, только функции. Так же нам не
# понадобились переменные уровня модуля. Тесты мы не стали писать, т.к. не
# добрались до темы тестирования. Осталось добавить main код.

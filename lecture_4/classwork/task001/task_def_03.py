# Аргументы функции
# Рассмотрим функцию с параметрами, т.е. принимающую на вход значения.
# Вспомним как в школе решали квадратные уравнения. Заодно разберём
# особенности создания функций в Python.
def quadratic_equations(a: int | float, b: int | float, c: int |
                                                           float) -> tuple[float, float] | float | str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *
                                                             a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'


print(quadratic_equations(2, -3, -9))

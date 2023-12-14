# 4. Декораторы functools
# Дополнительные возможности декорирования предоставляет модуль functools
# декоратор.
# Декоратор wraps
# Рассмотрим код из прошлой главы, но добавим строку документации в функцию
# factorial.
import time
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result

        return wrapper

    return deco


@count(10)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)
# Вместо ожидаемого вывода документации о функции и её названия получаем
# информацию об обёртке wrapper:
# factorial.__name__ = 'wrapper'
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)

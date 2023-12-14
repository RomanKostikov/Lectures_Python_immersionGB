# 1. Основы doctest
# Разработка через тестирование, TDD
# ➢ Написать код
# Самое время написать несколько строчек кода внутри функции is_prime(). На
# выходе получим следующий файл:
def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
# Понадобилось написать шесть строк кода, три проверки.
# 1. Убедиться что число целое, иначе вызвать ошибку типа.
# 2. Убедиться, что число не меньше двух, иначе вызвать ошибку значения. Тут мы
# проходим сразу два теста из пяти добавленных в техзадании.
# 3. Убедиться, что число меньше ста миллионов, иначе вывести
# предупреждение. Снова закрываем два теста одной проверкой
# ➢ Запуск всех тестов: убедиться, что все тесты проходят
# Запуск кода без режима verbose ничего не выводит. Код успешно проходит тесты. С
# режимом отображения увидим успешное прохождение всех семи тестов:
# ...
# 7 passed and 0 failed.
# Test passed.
# Ура! Мы успешно справились с поставленной задачей.

# Сравнение тестов doctest и unittest
# Возьмём уже знакомую функцию проверки числа на простоту и реализуем
# написанные ранее в doctest тесты используя unittest.
# Файл prime.py без тестов doctest
def is_prime(p: int) -> bool:
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than one')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
# Ничего нового в коде функции нет.

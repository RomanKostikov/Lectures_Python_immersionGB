# 3. Основы тестирования с pytest
# Файл test_prime_pt.py с кейсами pytest
import pytest
from prime_pytest import is_prime


def test_is_prime():
    assert not is_prime(42), '42 - составное число'
    assert is_prime(73), '73 - простое число'


def test_type():
    with pytest.raises(TypeError):
        is_prime(3.14)


def test_value():
    with pytest.raises(ValueError):
        is_prime(-100)


def test_value_with_text():
    with pytest.raises(ValueError, match=r'The number P must be greater than 1'):
        is_prime(1)


def test_warning_false(capfd):
    is_prime(100_000_001)
    captured = capfd.readouterr()
    assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'


def test_warning_true(capfd):
    is_prime(100_000_007)
    captured = capfd.readouterr()
    assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'


if __name__ == '__main__':
    pytest.main(['-v'])
# Начало с импортом и конец с запуском тестов стандартные для Python. Разберём
# каждый из кейсов.
# ➢ Кейс test_is_prime
# Проверяем базовую работу функции. Утверждение assert not ожидает получить
# ложь в качестве результата вызова функции. Второй assert ожидает получить
# истину.
# 🔥 Важно! Если первая строка провалит тест, второй assert не будет вызван
# для проверки. Обычно внутри кейса пишут одно утверждения. В нашем случае
# можно разделить проверки на два отдельных кейса.
# ➢ Кейс test_type
# Используем менеджер контекста pytest.raises который ожидает получить ошибку
# TypeError при вызове is_prime с вещественным число в качестве аргумента.
# Наличие ошибки проходит тест, а её отсутствие - роняет. Строка, которая должна
# поднять ошибку - последняя строка внутри менеджера контекста. Дальнейший код
# не будет выполняться.
# 25
# ➢ Кейс test_value
# Тест работает аналогично проверки типа, но мы указали другую ошибку в
# менеджере и передали другое значение в функцию.
# ➢ Кейс test_value_with_text
# Более сложный подход к тестированию. Помимо ошибки в параметр match
# передаётся регулярное выражение. Если оно совпадёт с текстом ошибки, тест будет
# пройден.
# ➢ Кейсы test_warning_false и test_warning_true
# Внимание! Оба примера выходят за рамки основ pytest. Это скорее пример на
# будущее для самых любознательных.
# Кейс получает фикстуру capfd в качестве аргумента. capfd (capture file descriptors)
# является одной из встроенных в pytest фикстур, которая позволяет перехватывать
# потоки вывода и ошибок. Внутри кейса вызываем тестируемую функцию. Далее
# используем метод readouterr() для получение потоков в переменную captured. В
# финале сравниваем результат captured.out (потока вывода) с ожидаемым текстом
# сообщения.

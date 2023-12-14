# Основы тестирования с pytest
# Перед вами несколько строк кода. Напишите что должна делать программа, чтобы
# пройти тесты. У вас 3 минуты.
import pytest
from main import func


def test_1():
    assert func(4) == 0


def test_2():
    assert func(4, -4) == (1, 0)


def test_3():
    assert func(4, -10, -50) == (5, -2.5)


def test_4():
    assert func(1, 1, 1) is None


if __name__ == '__main__':
    pytest.main(['-v'])

# решали квадротное уровнение в func
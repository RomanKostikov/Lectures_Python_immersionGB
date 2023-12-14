# Запуск тестов doctest из unittest
# А что если тесты уже написаны в doctest? В этом случае можно создать функцию
# test_loader и добавить тесты doctest в перечень для тестирования. Изучите пример.
import doctest
import unittest
import prime


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests


if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)
# Объект tests используя метод addTests добавляет импортированный модуль prime.
# Для этого используется класс DocTestSuite из модуля doctest. А если необходимо
# тестировать документацию, используется класс DocFileSuite. Теперь функция
# unittest.main соберёт написанные раннее тесты doctest и запустит их.

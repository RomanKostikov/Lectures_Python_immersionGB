# 1. Что такое замыкания
# Замыкаем изменяемые и неизменяемые объекты
# В очередной раз внесём правки в пример кода:
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
# Во внешнюю функцию добавлен список names. При каждом вызове внутренней
# функции в список добавляется новое значение из параметра b и возвращается
# полное содержимое списка в виде строки. У каждой из двух функций hello и bye
# оказывается свой список names. Они не связаны между собой, но каждый хранит
# список имён до конца работы программы. Обратите внимание, что list является
# изменяемым типом данных. Что будет, если мы перепишем код и заменим list на
# неизменяемый str?

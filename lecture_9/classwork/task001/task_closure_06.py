# 1. Что такое замыкания
# Замыкаем изменяемые и неизменяемые объекты
# Что будет, если мы перепишем код и заменим list на
# неизменяемый str?
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
# Изменения способа получения строки c join для списка на конкатенацию для строки
# не принципиально. Но стоит помнить, что сложение строк более дорогая операция
# по времени и по памяти, особенно если она находится внутри цикла.
# Что более важно - неизменяемый тип данных у строки text. Без добавления строчки
# кода nonlocal text была бы получена ошибка UnboundLocalError: local variable 'text'
# referenced before assignment. Мы явно указали, что хотим обращаться к
# неизменяемому объекту для изменения его значения.
# Как можно изменить неизменяемое? Мы создаём новый объект и присваиваем ему
# старое имя. Старый объект будет удалён сборщиком мусора. А команда nonlocal
# сообщает Python, что изменения ссылки на объект должны затронуть область
# видимости за пределами функции add_two_str.
# Подведём промежуточный итог. Благодаря тому что в Python всё объект, а функции
# являются функциями высшего порядка, мы можем вкладывать во внешнюю
# функцию различные переменные и внутренние функции. Далее возвращая из
# внешней функции внутреннюю создаём замыкания.

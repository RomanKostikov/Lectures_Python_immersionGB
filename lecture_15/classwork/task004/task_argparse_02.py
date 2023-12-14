# 5. Модуль argparse
# Создаём парсер, ArgumentParser
# При создании экземпляра из класса ArgumentParser можно 13 различных
# аргументов. Но большинство из них имеют оптимальные настройки по умолчанию.
# Если что-то и стоит добавить, то дополнительное описание, которое выводится при
# вызове справки.
# import argparse
# parser = argparse.ArgumentParser(prog='average', description='My first argument
# parser', epilog='Returns the arithmetic
# mean')
# ...
# ● prog — заменяет название файла в первой строке справки на переданное имя,
# ● description — описание в начале справки
# ● epilog — описание в конце справки
# Выгружаем результаты, parse_args
# Метод parse_args может принимать на вход два аргумента:
# ● строку для анализа. По умолчанию это sys.argv
# ● объект для сохранения результатов. По умолчанию это класс Namespace.
# Класс наследуется от object, не имеет ничего лишнего, но добавляет удобный
# вывод ключей и значений, помещённых в него.
# Изменять значения по умолчанию приходится крайне редко, почти никогда.
import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser', epilog='Returns the arithmetic mean')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers =}')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')
r"""
$ python .\task_argparse_02.py --help
$ python .\task_argparse_02.py 42 3.14 73
"""
# В этом случае код говорит сам за себя. Прочитайте три нижние строки. Уверен, что
# вопрос не должно остаться.

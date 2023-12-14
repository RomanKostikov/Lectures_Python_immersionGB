# 5. Модуль argparse
# Необязательные аргументы и значения по умолчанию
# Изменим наш парсер и добавим ещё несколько параметров к аргументам.
import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('-a', metavar='a', type=float, help='enter a for ax^2+bx+c=0', default=1)
    parser.add_argument('-b', metavar='b', type=float, help='enter b for ax^2+bx+c=0', default=0)
    parser.add_argument('-c', metavar='c', type=float, help='enter c for ax^2+bx+c=0', default=0)
    args = parser.parse_args()
    print(quadratic_equations(args.a, args.b, args.c))

r""""
python .\task_argparse_04.py -a 2 -b -12
python .\task_argparse_04.py -h
"""
# Вызов: $ python main.py -a 2 -b -12
# Теперь необходимо указывать ключи а, б и с при передаче значений. Но
# дополнительный параметр default позволяет отказаться от передачи. В этом случае
# значения будут взяты из параметра по умолчанию.

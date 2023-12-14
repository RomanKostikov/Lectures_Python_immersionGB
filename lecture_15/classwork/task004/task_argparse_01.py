# 5. Модуль argparse
# В финале поговорим о модуле argparse. Мы упоминали его, когда речь шла о запуске
# скриптов с параметром через sys.argv. Поговорим о том чем же argparse лучше argv.
# Спойлер — всем. Модуль argparse по сути надстраивается над sys.argv. Он
# генерирует справку, определяет способ анализа аргументов командной строки,
# сообщает об ошибках и даёт подсказки. Чтобы разобраться во всём перечисленном
# по традиции рассмотрим простой пример.
import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float,
nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')
# python .\task_argparse_01.py 42 3.14 73
# python .\task_argparse_01.py --help
# 💡 Внимание! Тут и далее до конца главы запускать файл будет из
# терминала ОС. Примерно так:
# $ python main.py ...
# 💡 где многоточие - передаваемые скрипту аргументы
# Запустим скрипт с несколькими значениями:
# $ python3 main.py 42 3.14 73
# На выходе получаем объект Namespace(numbers=[42.0, 3.14, 73.0]). Как
# это работает?
# 1. Создаём объект парсер при помощи класса ArgumentParser с
# первоначальными настройками экземпляра.
# 2. Добавляем в полученный экземпляр аргументы для парсинга через метод
# add_argument. Количество аргументов может быть любым. И каждый может
# содержать свои настройки.
# 3. Выгружаем результаты, переданные при запуске скрипта в терминале и
# обработанные парсером в виде объекта Namespace. Для этого вызываем
# метод экземпляра parse_args.
# Прежде чем разобрать каждый пунктов подробнее запустим скрипт ещё пару раз: с
# ключом --help и с каким-нибудь текстом.
# Ключ --help или -h
# После создания экземпляра парсера и задания ему аргументов формируется
# справочный текст. argparse добавляет ключи --help (длинная версия) и -h (короткая
# версия) автоматически. Другие ключевые параметры мы можем создать сами, но о
# них чуть позже.
# usage: main.py [-h] [N ...]
# My first argument parser
# positional arguments:
# N press some numbers
# options:
# -h, --help show this help message and exit
# Первая строка даёт общее представление о строке запуска. Ниже идёт текст,
# который мы указали в по ключу description при создании экземпляра. Далее
# получаем информацию о позиционных аргументах. В нашем случае это аргумент N
# (metavar='N') и подсказки к нему (help='press some numbers'). В конце идёт
# необязательные параметры, в нашем случае - автоматически сгенерированный
# вызов помощи.
# Запуск с неверными аргументами
# При попытке передать в скрипт Hello world! получим:
# usage: main.py [-h] [N ...]
# main.py: error: argument N: invalid float value: 'Hello'
# При создании аргумента мы указали, что хотим получать целые числа (type=float).
# Парсер автоматически создал валидатор и сообщил о несовпадении типов.
# Заметьте, что при передаче целых чисел ошибок не было, но они были
# преобразованы к вещественному типу.

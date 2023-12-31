# Урок 15. Обзор стандартной библиотеки Python

## Classwork

### Теория:

#### 1. Обзор библиотеки целиком

Мы уже упоминали стандартную библиотеку Python на курсе. Даже использовали
некоторый пакеты из неё. Вспомним, что же это такое.
Стандартная библиотека Python (The Python Standard Library) — распространяется
вместе с интерпретатором Python. Следовательно для использования пакетов и
модулей из неё достаточно написать import name.
Предлагаю для краткости называть Стандартную библиотеку Python просто
библиотека в рамках этой лекции.
Библиотека очень обширна и позволяет решать огромный спектр задач. Внутри есть
модули написанные на языке C. Благодаря ним у разработчиков есть лёгкий доступ
к системным функциям. Другие модули написаны на Python и предлагают готовые
решения для повседневных задач программирования.
Библиотека содержит:
● Встроенные функции
● Встроенные константы
● Встроенные типы
● Встроенные исключения
● Услуги обработки текста
● Службы двоичных данных
● Типы данных
● Числовые и математические модули
● Модули функционального программирования
● Доступ к файлам и каталогам
● Сохранение данных
● Сжатие данных и архивирование
● Форматы файлов
● Криптографические услуги
● Общие службы операционной системы
● Параллельное выполнение
● Сеть и межпроцессное взаимодействие
● Обработка данных в Интернете
● Инструменты обработки структурированной разметки
● Интернет-протоколы и поддержка
● Мультимедийные услуги
● Интернационализация
● Программные фреймворки
● Графические пользовательские интерфейсы с Tk
● Инструменты разработки
● Отладка и профилирование
● Упаковка и распространение программного обеспечения
● Службы выполнения Python
● Пользовательские интерпретаторы Python
● Импорт модулей
● Языковые службы Python
● Специальные службы MS Windows
● Специальные службы Unix
● Замененные (устаревшие) модули
И под каждым пунктом кроется несколько пакетов для решения соответствующих
теме задач. Вы можете перейти по ссылке и увидеть детальный состав библиотеки
самостоятельно https://docs.python.org/3.11/library/index.html.
Далее в рамках лекции рассмотрим несколько полезных модулей.

#### Уровни логирования

Уровень debug — отличная альтернатива функции print()

● NOTSET, 0 — уровень не установлен. Регистрируются все события.
● DEBUG, 10 — подробная информация, обычно представляющая интерес только при диагностике проблем.
● INFO, 20 — подтверждение того, что все работает так, как ожидалось.
● WARNING, 30 — указание на то, что произошло что-то неожиданное, или указание на какую-то проблему
в ближайшем будущем (например, «недостаточно места на диске»). Программное обеспечение попрежнему работает, как
ожидалось.
● ERROR, 40 — из-за более серьезной проблемы программное обеспечение не может выполнять некоторые
функции.
● CRITICAL, 50 — серьезная ошибка, указывающая на то, что сама программа не может продолжать работу.

#### Базовые регистраторы

В официальной документации указано, что работать
с регистраторами напрямую запрещено.

import logging
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

##### Свойства и методы для работы с datetime

Для получения доступа к свойствам используется точечная нотация.

Вывод по формату:
dt.timestamp()
dt.isoformat()
dt.strftime(FORMAT)
Получение из текстового формата:
datetime.fromtimestamp(text)
datetime.fromisoformat(number)
datetime.strptime(text, FORMAT)

#### Пара полезных структур данных Фабричная функция namedtuple из модуля collections

#### namedtuple принимает пару обязательных значений:

1. Имя класса. Это строка, содержащее точно такое же имя как
   и переменная слева от знака равно.
2. Список строк или строка с пробелами в качестве разделителей.
   Имена из списка превращаются в свойства класса.

#### Модуль array

● 'b' — целое со знаком, 1 байт
● 'B' — целое без знака, 1 байт
● 'u' — Юникод-символ в 2 или 4 байта
● 'h' — целое со знаком, 2 байта
● 'H' — целое без знака, 2 байта
● 'i' — целое со знаком, 4 байта
● 'I' — целое без знака, 4 байта
● 'l' — целое со знаком, 4 байта
● 'L' — целое без знака, 4 байта
● 'q' — целое со знаком, 8 байт
● 'Q' — целое без знака, 8 байт
● 'f' — вещественное обычной точности, 4 байта
● 'd' — вещественное двойной точности, 8 байт

#### Модуль argparse

Ключ --help или -h добавляется по умолчанию
import argparse
parser = argparse.ArgumentParser(description='My first
argument parser')
parser.add_argument('numbers', metavar='N', type=float,
nargs='*', help='press some numbers')
args = parser.parse_args()
Создаём парсер, ArgumentParser
Большинство настроек отлично работают со значениями по умолчанию
● prog — заменяет название файла в первой строке
справки на переданное имя,
● description — описание в начале справки
● epilog — описание в конце справки

##### Добавляем аргументы, add_argument

● metavar — имя, которое выводится с справке
● type — тип, для преобразования аргумента.
● nargs — указывает на количество значений, которые надо собрать из командной
строки и собрать результат в список list.
● help — вывод подсказки об аргументе.
● action — принимает одно из строковых значений и срабатывает при наличии в строке вызова скрипта
соответствующего параметра.
○ store_const — передаёт в args ключ со значением из параметра const
○ store_true или store_false — сохраняет в ключе истину или ложь
○ append — ищет несколько появлений ключа и собирает все значения после него в список
○ append_const — добавляет значение из ключа в список, если ключ вызван.

### task001:

- Модуль logging

### task002:

- Модуль datetime

### task003:

- Модуль collections
- Модуль array

### task004:

- Модуль argparse
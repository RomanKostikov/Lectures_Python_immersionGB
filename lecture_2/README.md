# Урок 2. Простые типы данных

## Classwork

### Теория:

#### Модуль typing

✔ Примитивы супер специального типа: Annotated, Any, Callable, ClassVar, Final, ForwardRef, Generic,
Literal, Optional, Protocol, Tuple, Type, TypeVar, Union
✔ Абсолютные типы из collections.abc: AbstractSet, ByteString, Container, ContextManager, Hashable,
ItemsView, Iterable, Iterator, KeysView, Mapping, MappingView, MutableMapping, MutableSequence,
MutableSet, Sequence, Sized, ValuesView, Awaitable, AsyncIterator, AsyncIterable, Coroutine, Collection,
AsyncGenerator, AsyncContextManager
✔ Структурные проверки, протоколы: Reversible, SupportsAbs, SupportsBytes, SupportsComplex,
SupportsFloat, SupportsIndex, SupportsInt, SupportsRound
✔ Коллекция конкретных типов: ChainMap, Counter, Deque, Dict, DefaultDict, List, OrderedDict, Set,
FrozenSet, NamedTuple, TypedDict, Generator
✔ Другие конкретные типы: BinaryIO, IO, Match, Pattern, TextIO
✔ Одноразовые вещи: AnyStr, cast, final, get_args, get_origin, get_type_hints, NewType, no_type_check,
no_type_check_decorator, NoReturn, overload, runtime_checkable, Text, TYPE_CHECKING

### Функции для получения информации об атрибутах и методах

**Функция dir(object)
Попытается вернуть список допустимых атрибутов для объекта.
Если объект не передавать — список имен в текущей локальной области
Функция help(object)
Если объект не указан, запускается интерактивная справочная система.
Если аргумент является строкой, то эта строка ищется как имя модуля,
функции, класса, метода, ключевого слова или раздела документации
и далее выводится страница справки. Если аргументом является объект
любого другого типа, создается страница справки по этому объекту**

### Целые числа

Разберём на примерах.
✔ int(x, base=10) — возвращает целочисленный
объект, созданный из числа или строки x ,
или возвращает значение 0, если аргументы
не заданы. base — основание системы счисления,
от 2 до 36.
✔ bin(x) — преобразует целое число в двоичную
строку с префиксом «0b».
✔ oct(x) — преобразует целое число в
восьмеричную строку с префиксом «0o».
✔ hex(x)— преобразует целое число в строчную
шестнадцатеричную строку с префиксом «0x».

### Логические типы, функция bool()

Разберём на примерах.
✔ bool(x) — возвращает логическое значение,
т.е. одно из двух: True или False

### Вещественные числа

Разберём на примерах.
✔ float(x) — возвращает число с плавающей
запятой, составленное из числа или строки x.

### Строки и способы их записи

str(object='') — возвращает строковую версию объекта.

📌 Три вида кавычек
txt = 'Книга называется "Война и мир".'
class str(object):
"""
str(object='') -> str
str(bytes_or_buffer[, encoding[,
errors]]) -> str
...
"""

📌 Склеивание и обратный слеш
text = 'Привет.' 'Как ты, друг?' 'Рад тебя
видеть.'
very_long_text = 'Lorem ipsum dolor sit amet,
consectetur adipisicing elit. A ab alias animi
assumenda at aut ' \
'commodi, consequatur cumque
ea harum, hic id illum ipsam itaque laboriosam
magnam minus nam nulla ' \
'numquam obcaecati officia
officiis porro possimus praesentium quaerat
temporibus ullam veniam? '

### Размер строки в памяти

object.__sizeof__() — метод возвращает
размер объекта в байтах
empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

### Методы проверки строк

str.isalnum() — возвращает True, если все символы в строке буквенно-цифровые. Символ является
буквенно-цифровым, если одно из следующих значений возвращает True: c.isalpha(), c.isdecimal(),
c.isdigit()или c.isnumeric().
✔ str.isalpha() — возвращает True, если все символы в строке являются буквенными. Алфавитные
символы — это символы, определенные в базе данных символов Юникода как «буква».
✔ str.isdecimal() — возвращает True, если все символы в строке являются десятичными символами
✔ str.isdigit() — возвращает True, если все символы в строке являются цифрами. Цифры включают
десятичные символы и цифры, требующие специальной обработки, например цифры надстрочного
индекса совместимости.
✔ str.isnumeric() — возвращает True, если все символы в строке являются числовыми символами.
Числовые символы включают цифровые символы и все символы, которые имеют свойство
числового значения Unicode.
✔ str.isascii() — возвращает True, если строка пуста или все символы в строке ASCII.
✔ str.islower() — возвращает True, если все символы в строке в нижнем регистре.
✔ str.istitle() — возвращает True, если строка является строкой с заглавным регистром
и содержит хотя бы один символ.
✔ str.isupper() — возвращает True, если все символы в строке в верхнем регистре.
✔ str.isprintable() — возвращает True, если все символы в строке доступны для печати или строка пуста.
Непечатаемые символы — это символы, определенные в базе данных символов Unicode как «Другие»
или «Разделители», за исключением пробела ASCII (0x20), который считается печатаемым.
✔ str.isspace() — возвращает True, если в строке есть только пробельные символы.

### Математика в Python

### Математические модули

В Python есть несколько модулей в стандартной
библиотеке, которые облегчают математические
расчёты. Для доступа к ним необходимо выполнить
импорт в начале файла.
import math
import decimal
import fractions

### task001:

* Простые типы данных и коллекции
* Изменяемые и неизменяемые типы
* Хэш hash() как проверка на неизменяемость

### task002:

* Изменяемые и неизменяемые типы
* Хэш hash() как проверка на неизменяемость

### task003:

* Аннотация типов

### task004:

* Атрибуты объекта

### task005:

* Простые объекты
* Целые числа, функция int()

### task006:

* Строки и способы их записи

### task007:
* Математические модули
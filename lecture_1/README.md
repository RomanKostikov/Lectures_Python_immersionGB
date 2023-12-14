# Урок 1. Основы Python

## Classwork

### Теория:

pip install requests
● pip freeze
● pip freeze > requirements.txt
○ more requirements.txt
● pip install -r requirements.txt

### Snake_case(основной стиль питонистов)

Верно
first_name
user_1, request
_tmp_name
min_step_shift

### Константы

Дополнительных команд для создания констант в языке Python нет!
Создаваемые
MAX_COUNT = 1000
ZERO = 0
DATA_AFTER_DELETE = 'No data'
DAY = 60 * 60 * 24

Встроенные
True — истина
False — ложь
None — ничего

### Функция id()

Функция id() возвращает адрес объекта
в оперативной памяти вашего компьютера
a = 5
print(id(a))
a = "hello world"
print(id(a))
a = 42.0 * 3.141592 / 2.71828
print(id(a))

### Зарезервированные слова

Базовый синтаксис языка Python образуют
нижеперечисленные зарезервированные слова:
False, None, True, and, as, assert, async,
await, break, class, continue, def, del, elif,
else, except, finally, for, from, global, if,
import, in, is, lambda, nonlocal, not, or,
pass, raise, return, try, while, with, yield.
А также case и match начиная с версии Python 3.10.

### Ввод и вывод данных

Вывод, функция print()
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Ввод, функция input()
result = input([prompt])

### Антипаттерн «магические числа»

Магическое число — это оперирование явно
указанными в коде коэффициентами
(как правило целочисленными), значение
и смысл которых знает только автор программы.
Считается плохим стилем с 1960-х годов!
age = float(input('Ваш возраст: '))
how_old = age - 18
print(how_old, "лет назад ты стал
совершеннолетним")

### Операции сравнения

В Python доступны шесть операций сравнения:
● «==» — равно
● «!=» — не равно
● «>» — больше
● «<=» — меньше или равно
● «<» — меньше
● «>=» — больше или равно

### Зарезервированные слова

● Если, if
● Иначе, else
● Ещё если, elif
● Выбор из вариантов, match и case

### Логические конструкции

В Python доступны три логических оператора:
● and — логическое умножение «И»;
● or — логическое сложение «ИЛИ»;
● not — логическое отрицание «НЕ».

### Логический цикл while
Разберём на примерах
● Начало цикла, while
● Возврат в начало цикла, continue
● Досрочное завершение цикла, break
● Действие после цикла, else

### Цикл итератор for in
Разберём на примерах
● Начало цикла, for in
● Цикл по целым числам,
он же арифметический цикл,
функция range()
● Цикл с нумерацией элементов,
функция enumerate()

### task001:
Основы python

### task002:
Ветвление 

### task003:
Циклы
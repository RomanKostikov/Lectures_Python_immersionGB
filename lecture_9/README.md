# Урок 9. Декораторы

## Classwork

### Теория

#### Термины лекции

● Замыкание (англ. closure) в программировании — функция первого класса,
в теле которой присутствуют ссылки на переменные, объявленные вне тела
этой функции в окружающем коде и не являющиеся её параметрами.
● Декоратор — структурный шаблон проектирования, предназначенный для
динамического подключения дополнительного поведения к объекту.

#### Замыкаем изменяемые и неизменяемые объекты

Вспоминаем mutable и immutable
● nonlocal immutable
явно указываем на необходимость изменения неизменяемого
типа данных за пределами функции

#### Передача функции в качестве аргумента

Функция может принимать другую функцию в качестве параметра
def main(func):
def wrapper(*args, **kwargs):
...
result = func(*args, **kwargs)
...
return result
return wrapper
def my_func(data):
...
return wrapper
deco = main(my_func)

#### Синтаксический сахар Python, @

Символ @ является более простым способом создать замыкание
def main(func):
def wrapper(*args, **kwargs):
...
result = func(*args, **kwargs)
...
return result
return wrapper
@main
def my_func(data):
...
return wrapper

#### Множественное декорирование

Функция может быть декорирована одновременно несколькими декораторами
@deco_c
@deco_b
@deco_a
def my_func(data):
...
return wrapper

#### Дополнительные переменные в декораторе

Аналогично замыканию переменных в функции,
декоратор может замыкать переменные в себе
def main(func):
closure = []
def wrapper(*args, **kwargs):
...
result = func(*args, **kwargs)
...
return result
return wrapper

#### Декоратор с параметрами

Три уровня вложенности позволяют передавать аргументы в декоратор
def count(param):
def deco(func: Callable):
def wrapper(*args, **kwargs):
...
return result
return wrapper
return deco

#### Декораторы functools

Декоратор wraps
def count(param):
def deco(func: Callable):
@wraps(func)
def wrapper(*args, **kwargs):
...
return result
return wrapper
return deco
✔ __name__ получает имя декорируемой функции
✔ help() возвращает справку декорируемой функции

#### Декоратор cache

cache позволяет кэшировать результат работы функции
@cache
def my_func(data):
...

### task001:

- Замыкание

### task002:

- декоратор

### task003:

- декоратор с параметром

### task004:

- Декораторы functools

## Homework

### task001:

Задание

1. Примените рассматриваемые на лекции
   декораторы к функциям, созданным
   на прошлых уроках.
2. Попробуйте создать свои декораторы.
   Например вы можете написать
   декоратор, который считает количество
   вызовов функции.
# Аннотация типов в функциях
# Начиная с Python 3.10 возможности указания типов расширились. Например можно
# указать несколько типов через вертикальную черту. Первый пример из этой главы
# можно записать так:
a: int | float = 42
b: float = float(input('Введи число: '))
a = a / b


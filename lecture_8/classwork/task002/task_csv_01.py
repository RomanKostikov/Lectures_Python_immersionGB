# Формат CSV
# При работе с CSV стоит помнить о том, что формат не до конца стандартизирован.
# Например запятая как символ разделитель может являться частью текста. Чтобы не
# учитывать такие запятые, можно использовать кавычки. Но тогда кавычки не могут
# быть частью строки. Кроме того десятичная запятая используется для записи
# вещественных чисел в некоторых странах. Все эти особенности необходимо
# учитывать при работе с CSV файлами.
# В первой строке могут содержаться заголовки столбцов как в нашем случае. Строки
# со второй и до конца файла представляют записи. Одна строка — одна запись.
# Текстовая информация заключена в кавычки, а числа указаны без них.
# Подобные текстовые CSV файлы легко получить выгрузив данные из Excel или
# другой электронной таблицы указав нужный формат. По сути CSV является
# промежуточным файлом между Excel и Python.

# ● Чтение CSV
# Функция csv.reader принимает на вход файловый дескриптор и построчно читает
# информацию.
import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))
# 🔥 Важно! При работе с CSV необходимо указывать параметр newline=’’ во
# время открытия файла
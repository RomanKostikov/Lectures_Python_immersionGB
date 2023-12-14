# Формат CSV
# ● Чтение в словарь
# Помимо сохранения таблицы в список можно использовать для хранения словарь.
# Ключи словаря — названия столбцов, значения — очередная строка файла CSV.
# Прочитаем файл biostats_tab.csv из примера выше, но не в список, а в словарь.
# Воспользуемся классом DictReader.
import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restkey="new", restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# Формат CSV
# ● Чтение в словарь
import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex",
                                             "age", ], restkey="new", restval="Main Office",
                              dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')
# Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
# берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
# элементы списка в restkey ключ.

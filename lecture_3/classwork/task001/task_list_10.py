# Работа со списками
# Сортировка списков
# Одна из частых операций при работе со списками их сортировка. Python позволяет
# отсортировать список на месте, inplace, т.е. не создавая копию. А можно создать
# копию отсортированного списка как отдельный объект.


my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
my_list.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'
res = sorted(my_list)  # TypeError: '<' not supported between instances of 'int' and 'str'

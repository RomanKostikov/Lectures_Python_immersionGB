# Работа со списками
# Метод extend
a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a)  # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)

# ● extend(a) — если в метод передать не коллекцию, получим ошибку TypeError.
# ● extend(b) — строка воспринимается как коллекция, в результате каждый
# символ строки помещается в новую ячейку списка.
# 9
# ● extend(c) — итерируемся по списку, c последовательно добавляя его
# элементы в список my_list
# ● extend(my_list) — удваиваем список, добавляя копию всех его элементов

# Множества set и frozenset
# Методы множеств
# Рассмотрим некоторые методы множеств на примере изменяемого множества set.
# Все методы, которые не изменяют оригинал, работают аналогично и для множества
# frozenset.
# Метод add
# Метод add работает аналогично методу списка append, т.е. добавляет один элемент
# в коллекцию.
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10)  # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set)

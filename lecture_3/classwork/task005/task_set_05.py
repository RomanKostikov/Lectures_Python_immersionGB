# Множества set и frozenset
# Методы множеств
# Метод intersection
# Для получения пересечения множеств, т.е. множества с элементами, которые есть и
# в левом и в правам множестве используют метод intersection
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# Новая версия Python позволяет получить пересечение множеств в следующей
# записи c использованием символа &
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')


# Словарь, dict
# Метод popitem
# Для удаления пары ключ значение из словаря используют метод popitem.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')
# Так как словари сохраняют порядок добавления ключей, удаление происходит
# справа налево, по методу LIFO. Элементы удаляются в обратном добавлению
# порядке.

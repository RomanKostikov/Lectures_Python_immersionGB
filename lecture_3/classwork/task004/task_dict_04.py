# Словарь, dict
# Доступ к значению словаря
# Доступ через метод get
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))
# При обращении к существующему ключу метод get работает аналогично доступу к
# через квадратные скобки. Если обратиться к несуществующему ключу, get
# возвращает None. Метод get принимает второй аргумент, значение по умолчанию.
# Если ключ отсутствует в словаре, вместо None будет возвращено указанное
# значение.

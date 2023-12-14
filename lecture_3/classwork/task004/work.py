# Словари, dict
# Погружение в Python | Коллекции
my_dict = {'one': 1,
 'two': 2,
 'three': 3,
 'four': 4,
 'ten': 10,
 }
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)
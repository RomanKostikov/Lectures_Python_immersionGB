# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты. Четыре попытки ввода пользователя указаны ниже кода
d = {'42': 73}
try:
    key, value = input('Ключ и значение: ').split()
    if d[key] == value:
        r = 'Совпадение'
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
else:
    print(r)
finally:
    print(d)
# >>> Ключ и значение: 42 13 # NameError: name 'r' is not defined
# >>> Ключ и значение: 42 73 3 # too many values to unpack (expected 2)
# {'42': 73}
# >>> Ключ и значение: 73 42 # KeyError: 73
# >>> Ключ и значение: 42 73 # NameError: name 'r' is not defined при вводе это строка, а исходное число

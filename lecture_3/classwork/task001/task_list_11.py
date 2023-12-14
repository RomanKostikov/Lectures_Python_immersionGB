# Работа со списками
# Функция sorted().
# Переданная в функцию коллекция остаётся неизменной после результата работы
# функции. Если в функцию передать дополнительный аргумент reverse=True,
# сортировка происходит по убыванию.

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')

# Работа со списками
# Метод insert
# Метод insert принимает на вход два аргумента — индекс для вставки и объект
# вставки. Метод добавляет элемент после индекса.
my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73)  # my_list.append(73)
print(my_list)

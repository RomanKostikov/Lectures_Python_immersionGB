# Работа со списками
# Метод append
a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)

print(my_list)
my_list.append(c)
print(my_list)
my_list.append(my_list)
print(my_list)
# Вывод: [None, 42, 'Hello world!', [1, 3, 5, 7], [...]]

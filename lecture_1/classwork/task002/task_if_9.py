# Проверка на вхождение, in
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')

# А теперь тот же самый код, но с конструкцией not — отрицание:
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Введи число: '))
# if num not in data:
#     print('Леонардо грустит :-(')
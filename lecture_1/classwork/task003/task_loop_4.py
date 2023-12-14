# Действие после цикла, else
min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))

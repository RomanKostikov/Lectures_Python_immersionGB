#  многоуровневое условие
pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Доступ запрещён')
print('Работа завершена')

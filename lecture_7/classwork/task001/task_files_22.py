# Методы перемещения в файле
# При работе с файлом можно управлять положением файлового объекта в открытом
# файле. Действия напоминают движение курсора в строке стрелками влево и
# вправо.
# ● Метод tell
# Метод tell возвращает текущую позицию в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
print(f.tell())
print(f.tell())  # ValueError: I/O operation on closed file.
# Для пустого файла возвращается ноль — начало файла. По мере записи или чтения
# информации позиция сдвигается к концу файла.
# Метод использую для определения в каком месте файла будет произведены чтение
# или запись.

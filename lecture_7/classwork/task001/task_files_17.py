# Запись и добавление в файл
# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')

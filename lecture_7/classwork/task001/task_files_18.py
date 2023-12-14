# Запись и добавление в файл
# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')

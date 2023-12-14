# Запись и добавление в файл
# ● Запись методом writelines
# Метод writelines принимает в качестве аргумента последовательность и записывает
# каждый элемент в файл. Элементы последовательности должны быть строками или
# байтами в зависимости от режима записи.
# В отличии от write этот метод ничего не возвращает.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
# Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
# воспользовались строковым методом join. writelines не добавляет переноса между
# элементами последовательности.

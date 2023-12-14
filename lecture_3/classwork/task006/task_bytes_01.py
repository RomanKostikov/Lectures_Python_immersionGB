# Классы bytes и bytearray
# Уделим несколько строк лекции неизменяемым байтам и их изменяемой версии —
# массиву байт. Для отправки информации по каналам связи объекты не подойдут.
# Даже текст не отправить. А вот пересылать байты — легко.
text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
# Строковой метод encode получает в качестве аргумента указание кодировки. На
# выходе получаем строку байт. Функция print возвращает строковое представление
# байт, сами ячейки памяти с электронами невозможно увидеть невооруженным
# глазом.
# Префикс b говорит о том, что перед нами не строка, а байты. Если байт может быть
# представлен как символ, т.е. он есть в семибитной кодировке ASCII. отображается
# символ. В остальных случаях указывается приставка \x и слитно с ней
# шестнадцатеричное представление байта.
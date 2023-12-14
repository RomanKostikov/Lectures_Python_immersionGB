# Строки, str
# Методы count, index, find
# Как и у списка, строка поддерживает методы count для подсчёта вхождения и index
# для поиска элемента. Но у строки появился и новый метод find. Он работает
# аналогично index. Но если искомая подстрока отсутствует, вместо ошибки
# возвращает -1.
text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))


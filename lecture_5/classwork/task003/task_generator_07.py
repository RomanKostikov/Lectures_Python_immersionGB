# Генераторы
# Set comprehensions
# Кроме синтаксического сахара для генерации списков можно создавать множества
# в одну строку. Синтаксис аналогичен примерам выше. Изменяются лишь скобки.
# Для множеств используются фигурные.
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

# Мы также перебираем элементы в цикле. Также можно использовать вложенные
# циклы. Также для каждого цикла может быть проверка на включение элемента в
# множество.
# Стоит обратить внимание на следующие особенности:
# ● порядок элементов внутри множества может не совпадать с порядком
# добавления элементов.
# ● множество хранит только уникальные значения
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
# Как и в примерах выше для генерации множества перебрали все возможные
# комбинации пар x и y списков. Но в итоге осталось не 25 элементов, а 19
# уникальных. 6 дублирующих элементов не были добавлены в множество, но время
# на их обработку было затрачено. Асимптотика не улучшилась.


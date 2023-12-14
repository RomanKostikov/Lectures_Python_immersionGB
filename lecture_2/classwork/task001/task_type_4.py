# Функция isinstance()
data = 42
print(isinstance(data, int))
# Получили True, т.к. 42 — целое число.

data = True
print(isinstance(data, int))

# Снова истина, т.к. логический объект True в Python подклассом, основанном на
# классе int. Проверка может проходить сразу по нескольким классам. В этом случае
# истину вернётся, если объект является экземпляром любого из переданных в
# кортеже классов.

data = 3.14
print(isinstance(data, (int, float, complex)))

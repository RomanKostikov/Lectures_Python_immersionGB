# Модуль array
# Массивы поддерживают методы списка list, поэтому использование их интуитивно
# понятно. Привыкать надо лишь к указанию хранимого типа данных.
from array import array
long_array = array('l', [-6000, 800, 100500])
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())
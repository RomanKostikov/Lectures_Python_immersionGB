# Модуль array
# Так же будет поднята ошибка при
# несоответствии типа.
from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(2 ** 32)  # OverflowError: Python int too large to convert to C long
long_array.append(3.14)  # TypeError: 'float' object cannot be interpreted as an integer
# Массивы array являются более экономичной по памяти структурой данных, чем
# списки list.

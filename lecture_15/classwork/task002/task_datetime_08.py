# 3. Модуль datetime
# А теперь несколько обратных методов, позволяющих создать объекты datetime.
from datetime import datetime

date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. '
                                         'День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date)
print(timestamp_date)
print(iso_date)
print(text_date)
# ● fromisoformat — метод анализирует строку текст и если она совпадает со
# стандартом ISO 8601, возвращает объект datetime. Стандартный вывод
# объектов на печать позволяет делать обратное преобразование этим
# методом.
# ● fromtimestamp — получаем объект даты из целого или вещественного числа.
# Само число — количество секунд после полуночи 1 января 1970.
# ● strptime — метод принимает на вход два параметра: строку для
# преобразования и строку с форматом. Если формат позволяет
# проанализировать строку, возвращается объект datetime.

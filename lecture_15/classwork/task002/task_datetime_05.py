# 3. Модуль datetime
# Доступ к свойствам
# Каждый из объектов позволяет прочитать хранимые свойства обратившись к ним
# по имени через точечную нотацию.
from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101, seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')
# Даже если свойство явно не передано, но объект хранит его, мы можем получить
# доступ на чтение.
# Изменить значение напрямую не получится. Всё же перед нами неизменяемые
# объекты. Но мы можем воспользоваться методом replace для создания копии со
# значениями текущего объекта. Изменения затронут только указанные параметры.
# 💡 Внимание! timedelta не имеет метода replace.

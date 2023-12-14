# 3. Модуль datetime
# Математика с датами
# Разница во времени появляется при математических операциях с датами и
# временем. И этажа разница может использоваться для изменения дат. Например
from datetime import datetime, timedelta

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')

birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')
# В первом случае нашли разницу во времени между двумя событиями. А во втором
# вычислили дату тридцатитрёхлетия

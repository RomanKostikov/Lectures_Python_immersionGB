# Математика в Python
# Модуль decimal

import decimal

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

decimal.getcontext().prec = 5
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

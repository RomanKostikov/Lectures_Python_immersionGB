# 4. Математика и логика в классах
# Вычисление процентов вместо нахождения
# остатка от деления, __imod__
# Создадим простой класс Money, который будет увеличивать значение на указанный
# процент при записи Money %= float | int
from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self
    

m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)
# Для точности вычислений используется класс Decimal. Поэтому при увеличении на
# указанный процент используем дополнительное обёртывание правого значение в
# Decimal.
# 🔥 Важно! Не забывайте return self при работе с in place дандер методами.

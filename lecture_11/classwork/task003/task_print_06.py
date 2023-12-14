# 3. Представления экземпляра
# Приоритет методов
# Как же получить вывод от
# __repr__ при наличии двух методов? Есть несколько способов вывода на печать:
# сработает.
class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней- {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'
    

user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
print(f'{user}')
print(repr(user))
print(f'{user = }')
# В первых двух вариантах срабатывает дандер __str__. Далее мы явно передаём в
# print результат встроенной функции repr, которая обращается к одноимённому
# методу. Так же при использовании f-строк символ равенства выводит имя
# переменной слева от знака равно и repr справа от него.

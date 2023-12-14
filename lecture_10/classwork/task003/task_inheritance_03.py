# 3. Наследование
# Переопределение методов
# При наследовании мы можем использовать в дочернем классе все общедоступные
# свойства и методы родительского класса. Кроме того можно создать свои. И если
# имена будут совпадать, произойдёт переопределение. Будут браться значения
# дочернего класса.

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)  # раскомментировать после первого запуска

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person('Маг', 'Тролль')

print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')

p1.add_many_up()
print(f'{p1.up = }')

# В примере создан метод change_health с дополнительным множителем. Он
# срабатывает у героя. Но при вызове метода у экземпляра класса Person
# срабатывает старый метод.
# В методе add_many_ups для обхода инкапсуляции используем запись
# self._Person__max_up. Экземпляр обращается к приватному атрибуту родительского
# класса, напрямую указав его.

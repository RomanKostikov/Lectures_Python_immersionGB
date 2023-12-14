# 1. Основы ООП в Python
# Методы класса
# При желании можно передавать в метод аргументы. И так как в Python всё объект,
# можно передать даже экземпляр класса.
class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# Метод change_health принимает ещё один экземпляр и количество здоровья.
# Атрибут надо изменить и у экземпляра, вызвавшего метод и у второго, переданного
# экземпляра.
# 🔥 Внимание! Чаще всего для указания на другой экземпляр того же класса
# используют параметр other в имени метода. Соответственно записи other.name
# аналогичны self.name, но изменяют другой, переданный экземпляр класса.

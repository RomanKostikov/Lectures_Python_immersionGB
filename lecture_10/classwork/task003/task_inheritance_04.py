# 3. Наследование
# Множественное наследование
# Python поддерживает множественное наследование. Класс может быть
# наследником сразу двух и более классов. В некоторых языках множественное
# наследование недоступно по причине усложнения кода. Например наследуя класс
# существо от классов птицы и рыбы позволит создать летающую рыбу или
# плавающую птицу?
# Рассмотрим вариант множественного наследования.
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


class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'


class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'


class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None,
                 country=None, city=None, street=None,
                 left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
          country='Эльфляндия', street='Ночного эльфа',
          left_hand='Стрела')
print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')

# Мы создали классы Address и Weapon. Добавив их к нашему герою, получаем
# сочетание атрибутов и методов всех перечисленных классов. Обратите внимание на
# то как происходит инициализация родительских классов внутри Hero __init__.
# Прописали все параметры из родительских классов в инициализации класса Hero.
# Далее вручную распределяем аргументы между методами __init__ каждого из
# родительских классов. Подобный приём не лучшая практика. При изменении
# параметров у родительских классов, дочерние могут перестать работать. При
# простых реализациях наследования достаточно функции super(). Обычно не стоит
# усложнять код до того состояния, когда внутренние механизмы не справляются с
# наследованием.

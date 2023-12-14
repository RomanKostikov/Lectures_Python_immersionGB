# 2. Инкапсуляция
# Два подчёркивания в начале
# Двойное подчёркивание делает свойство или метод приватным. При этом
# срабатывает механизм защиты имени за пределами класса.
# 🔥 Важно! Переменная с двумя подчёркиваниями в начале не может иметь
# более одного подчёркивания в конце имени. Двойное подчёркивание до и
# после имени — магическая переменная Python. Подобно __init__ такие имена
# зарезервированы для особых действий.
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


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')
p1.up = 1
print(f'{p1.up = }')
for _ in range(5):
    p1.add_up()
    print(f'{p1.up = }')

print(p1._Person__max_up)  # доступ получен(прочитаны приватные значения за пределами самого класса)
print(Person._Person__max_up)  # доступ получен(прочитаны приватные значения за пределами самого класса)
# has no attribute '__max_up'
# Переменная __max_up доступна внутри класса и его экземпляров. Мы используем
# её для увеличения количества жизней персонажа в методе add_up. Никаких
# проблем с доступом нет.
# Когда же пытаемся обратиться к свойству напрямую, получаем ошибку доступа к
# атрибуту. Аналогичные ошибки будут и при обращении к методу, начинающемуся с
# двух подчёркиваний.

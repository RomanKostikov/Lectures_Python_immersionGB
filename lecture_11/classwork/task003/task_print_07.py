# 3. Представления экземпляра
# Печать коллекций
# Однако метод __repr__ оказывается более приоритетным, если на печать выводится
# не один элемент, а коллекция элементов.
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


u_1 = User('Спенглер')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'],
           name='Стэнц')
ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
print(f'{ghostbusters}')
print(repr(ghostbusters))
print(f'{ghostbusters = }')
print(*ghostbusters, sep='\n')
# В приведённом примере список из трёх экземпляров при печати возвращает repr
# представление во всех четырёх рассмотренных способах. И только при распаковке
# списка через звёздочку функция print получает экземпляры напрямую и вызывает
# их дандер __str__.

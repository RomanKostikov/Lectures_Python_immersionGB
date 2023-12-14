# 3. Представления экземпляра
# Рассмотрим более сложный класс и его
# метод __repr__.
class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
# Мы снова получили строку, которую можно скопировать и создать экземпляр без
# внесения правок. При этом свойство life опущено в выводе, т.к. не влияет на
# создание экземпляра.

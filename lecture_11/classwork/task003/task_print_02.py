# 3. Представления экземпляра
# Представление для пользователя, __str__
# Дандер метод __str__ используется для получения удобного пользователю
# описания экземпляра.
class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'


user = User('Спенглер')
print(user)
# Метод __str__ обязан вернуть строку str. Обычно это строка содержит информацию
# о свойствах класса для понимания что за экземпляр перед нами. Упор делается на
# удобство чтения. Но и о краткости забывать не стоит.

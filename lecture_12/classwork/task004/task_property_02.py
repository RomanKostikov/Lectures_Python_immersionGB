# 4.Декоратор @ property
# ● Getter
# Декоратор property позволяет создавать “геттеры”. Это методы, которые выдают
# себя за свойства, позволяют прочитать результат, но блокируют возможность
# записи. Рассмотрим другой пример “геттера”.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
user.full_name = 'Стивен Хокинг'  # AttributeError: can't set attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# Теперь у пользователя есть два публичных свойства для имени и фамилии. Кроме
# того есть свойство (а не метод) для вывода полного имени, т.е. с фамилией. Все три
# свойства работают на чтение. А вот перезаписать полное имя мы не можем. Зато
# ничего не мешает изменить фамилию и получить обновлённое полное имя.

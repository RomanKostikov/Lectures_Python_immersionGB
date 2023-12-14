# 3. Создаём менеджер контекста with
# ● Действия при входе в менеджер контекста, __enter__
# Создадим класс DB для упрощения работы с базой данных.
import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor


db = DB('sqlite.db')
with db as cur:  # AttributeError: __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
# Экземпляр класса хранит имя базы, которое задаём один раз при получении
# экземпляра. Дополнительно запоминаем соединение и курсор. В момент создания
# экземпляра им присваиваем None.
# Дандер __enter__ определяет действия при входе в менеджер контекста. В нашем
# случае это установление соединения с базой данных и получение курсора. Сам
# курсор возвращаем в менеджер в переменную после as.
# Если запустить код, получим ошибку доступа к атрибуту. Менеджер отказывается
# работать без указания действий для выхода.

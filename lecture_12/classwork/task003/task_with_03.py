# 3. Создаём менеджер контекста with
# ● Действия при выходе из менеджера контекста, __exit__
# Добавим дандер метод __exit__ и пропишем в нём операции, обязательные при
# завершении работы с базой данных.
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

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
# Внутри __exit__ подтверждаем изменения, закрываем соединения с базой и
# обнуляем свойства экземпляра. Параметры дандер __exit__ содержат информацию
# о типе и значении ошибки и трассировку, если она возникла внутри менеджера.
# Если ошибок не было, все три параметра содержат None.

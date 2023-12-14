# Команда except
# Подобное поведение можно применить не только к функции input, но и к любой
# ситуации получения данных. Код ниже имитирует получение данных из источника
# (база данных, сайт, удалённыё сервер и т.п.).
from random import randint

MAX_COUNT = 5


def get_data():
    """Получает данные из источника."""
    if result := randint(0, 3):
        return result
    else:
        raise ConnectionError


count = 0
while count < MAX_COUNT:
    count += 1
    try:
        data = get_data()
        break
    except ConnectionError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')

print(data)  # noqa

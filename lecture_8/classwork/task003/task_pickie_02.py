# 3. Pickle
# Сериализация
# Преобразуем словарь из главы про JSON в набор байт средствами модуля pickle.
import pickle

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')

# Вызываем функцию dumps для преобразования всей структуры в строку байт.
# Отдельно указали протокол по умолчанию. Модуль pickle имеет несколько
# протоколов, который не гарантируют совместимость с более старыми версиями.
# Сейчас протоколом по умолчанию является версия 4. Она появилась в Python 3.4, а
# стала дефолтным протоколом с Python 3.8. Если вы не занимаетесь поддержкой
# старого кода, можно смело использовать четвёртую версию протокола.
# Попробуем сохранить объекты, неподдерживаемые JSON в бинарный файл.
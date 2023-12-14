# Модуль JSON
# ● Преобразование Python в JSON
# Что делать, если мы хотим превратить Словарь Python в JSON объект? Для этого
# используем функции сериализации dump и dumps. Смысл окончания s у dumps
# такой же как и у loads.
import json

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
print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)

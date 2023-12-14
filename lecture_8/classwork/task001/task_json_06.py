# Модуль JSON
# ● Преобразование Python в JSON
# Если же мы хотим отказаться от символов экранирования в JSON файле, следует
# установить дополнительный параметр ensure_ascii в значение ложь.
# Воспользуемся словарём my_dict ещё раз для проверки функции dumps
import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
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

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)

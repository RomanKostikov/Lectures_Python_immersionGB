# Модуль JSON
# ● Преобразование Python в JSON
# Как вы видите символы отличные от ASCII были заменены на специальные коды.
# Это не означает, что файл повреждён или что-то пошло не так. Проведём
# десериализацию уже знакомым способом и проверим целостность данных.
import json

with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')

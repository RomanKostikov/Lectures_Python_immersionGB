# Модуль JSON
# Для работы с форматом в Python есть встроенный модуль json. Для его
# использования достаточно импорта в начале файла:
# import json
# Рассмотрим четыре основных функции модуля.
# ● Преобразование JSON в Python
# Договоримся, что представленный выше объект JSON сохранён в виде текстового
# файла user.json в кодировке UTF-8 в той же директории, что и исполняемый код.
import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)
print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')

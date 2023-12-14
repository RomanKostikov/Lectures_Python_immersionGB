# Модуль JSON
# А теперь представим, что мы подготовили информацию в виде многострочного str в
# python и хотим превратить его из JSON строки в объекты Python.
import json

json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et
        accusantium",
        "body": "consectetur animi nesciunt iure dolore"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero quia laudantium autem",
        "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quibusdam tempore odit est dolorem",
        "body": "praesentium quia et ea odit et ea voluptas et"
    }
]"""
print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list =}')
# Функция loads принимает на вход строку хранящуюся как структуру JSON и
# преобразует её к нужным типам. В нашем примере получили список list с четырьмя
# словарями внутри.
# Запомнить различия между функциями просто. Окончание s у loads намекает на
# строку. А load требует объект с методом read для чтения информации. Напомним,
# что файловый дескриптор имеет метод read для чтения информации из файла.
# 🔥 Важно! При открытии файлов важно учитывать их размер. Огромные
# JSON объекты даёт высокую нагрузку на процессор и оперативную память.

# 1. Что такое замыкания
# Функция как объект высшего порядка
# Рассмотрим простой пример функции:
def add_str(a: str, b: str) -> str:
    return a + ' ' + b


print(add_str('Hello', 'world!'))

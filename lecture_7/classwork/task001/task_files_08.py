# Менеджер контекста with open
# Начиная с Python 3.10 менеджер контекста поддерживает круглые скобки для
# группировки нескольких операторов по строкам:
with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))

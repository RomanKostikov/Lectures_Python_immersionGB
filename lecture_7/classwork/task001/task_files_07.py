# Менеджер контекста with open
with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
        open('bin_data', 'rb') as f2, \
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))
# Обратите внимание на запятые между open. И при переносе кода на новую строку
# обязательно указывать обратную косую черту (бэкслеш). Так Python поймёт, что это
# одна длинная строка с переносами, а не несколько отдельных.

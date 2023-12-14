# 1. Обработка исключительных
# Посмотрите на код ниже.
def get(text: str = None) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
# Попробуем и тут ввести “сорок два”
# Введите целый делитель: сорок два
# Traceback (most recent call last):
# File "C:\Users\main.py", line 8, in <module>
# number = get('Введите целый делитель: ')
# File "C:\Users\main.py", line 3, in get
# num = int(data)
# ValueError: invalid literal for int() with base 10: 'сорок два'
# Process finished with exit code 1
# Ошибка точно такая же. Но теперь трассировка показывает, что ошибка возникла в
# третьей строке кода при приведении данных к целому типу. А чуть ранее мы
# вызвали функцию get в строке 8, которая и заставила выполнятся третью строчку
# кода.
# Чтение трассировки помогает найти источник ошибки. Python и тут проявляет
# максимальное дружелюбие к разработчику и даёт максимально возможное
# количество информации об ошибке. Если вы писали на других языках, скорее всего
# вы уже заметили это дружелюбие.

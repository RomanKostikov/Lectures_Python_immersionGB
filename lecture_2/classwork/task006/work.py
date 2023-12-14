# Напишите небольшую программу, которая
# запрашивает у пользователя текст.
# Если текст можно привести к целому числу,
# выведите его двоичное, восьмиричное
# и шестнадцатиричное представление.
# А если преобразование к целому невозможно,
# сообщите написан ли текст в ASCII или нет.
text = input("Введите текст: ")

try:
    num = int(text)
    binary = bin(num)
    octal = oct(num)
    hexadecimal = hex(num)
    print("Двоичное представление:", binary)
    print("Восьмиричное представление:", octal)
    print("Шестнадцатиричное представление:", hexadecimal)
except ValueError:
    if all(ord(c) < 128 for c in text):
        print("Текст написан в ASCII")
    else:
        print("Текст не написан в ASCII")
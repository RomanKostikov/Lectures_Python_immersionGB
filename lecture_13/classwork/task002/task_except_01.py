# Команда except
# Как вы верно догадались из текста синтаксической ошибки, команда try должна
# работать в связке с командой except или finally.
# Рассмотрим вариант обработки ошибки в нашем коде:
def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
        num = 1
        print(f'Будем считать результатом ввода число {num}')
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
# После зарезервированного слова except указывается класс ошибки, которую мы
# хотим обработать. Обычно используется запись вида except NameError as e: Таким
# образом в переменную e попадает информация об ошибке. Например для вывода
# её в консоль, сохранения в логи и т.п. В нашем случае при невозможности получить
# целое число из пользовательского ввода сообщаем ему об этом. Далее делаем вид,
# что была введена единица. Программа продолжает работать несмотря на ошибку.

# Команда finally
# Ещё одна команда для обработки исключений — finally. Она срабатывает во всех
# случаях. И если была ошибка и отработал блок except. И если ошибки не было.
def get(text: str = None) -> int:
    num = None
    try:
        num = int(input(text))
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
    finally:
        return num if isinstance(num, int) else 1


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    try:
        print(f'100 / {number} = {100 / number}')
    except ZeroDivisionError as e:
        print(f'На ноль делить нельзя. Получим {e}')
# Даём пользователю одну попытку на ввод числа. Независимо от результата
# сработает блок finally. Он вернёт либо целое число, либо единицу, если получить
# целое не удалось. Обработку деления на ноль вынесли в основной код.
# Обычно finally используют для действий, которые обязательны независимо от того
# была ошибка или нет.

# 4. Создание собственных исключений
# Дорабатываем код в файле error.
class UserException(Exception):
    pass


class UserAgeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Возраст пользователя должен быть целым int() или вещественным float() больше нуля.\n' \
               f'У вас тип {type(self.value)}, а значение {self.value}'


class UserNameError(UserException):
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = 'попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.lower:
            text = 'больше верхней'
        return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов).\n' \
               f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'
# В случае с возрастом просто получаем текущее значение в переменную value. Далее
# выводим информацию об ошибке без явного уточнения проблемы. Просто
# сообщаем о допустимых типе и значении, а также выводим переданное значение и
# его тип.
# При обработки ошибки имении дополнительно принимаем в инициализацию
# граничные значения длины. Переменная text внутри дандер __str__ получает
# значение в зависимости от границы: “меньше нижней” или “больше верхней”.
# Вывод точно указывает на то, в какую из границ мы не попали.
# 🔥 Внимание! В классе User надо исправит строку вызова ошибки имени,
# чтобы код сработал верно. Иначе исключение вернёт нам исключение
# TypeError: UserNameError.__init__() missing 2 required positional arguments:
# 'lower' and 'upper'

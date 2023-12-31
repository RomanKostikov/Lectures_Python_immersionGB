# Документирование кода функций
# Если описание функции подразумевает больше подробностей, после первой строки
# документации оставляют одну пустую. Далее в несколько строк даётся всё
# необходимое описание. Закрывающие кавычки ставятся на отдельной строке, без
# текста.
def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    ...
# Подобная запись автоматические помещает текст в переменную __doc__. Описание
# функции можно будет получить через вызов справки help с передачей функции в
# качестве аргумента.
help(max_before_hundred)

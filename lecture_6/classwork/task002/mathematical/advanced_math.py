# Создание пакетов и их импорт
# Продолжим нашу идею с учебным математическим модулем. Наш проект
# развивается и решено добавить целочисленное деление и возведение в степень. А
# чтобы модуль не разрастался до бесконечности, продвинутую математику будем
# хранить в отдельном файле advanced_math.py
"""Two advanced mathematical operations.
Integer division and exponentiation."""
__all__ = ['div', 'exp']
_BEGINNING = 0
_CONTINUATION = 1


def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res //= item
    return res


def exp(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res **= item
    return res


if __name__ == '__main__':
    print(f'{div(42, 4) = }')
    print(f'{exp(2, 4, 6, 8) = }')
# Самое время объединить два схожих модуля в один пакет. Создаём директорию
# mathematical и переносим в неё оба файла: base_math,py и advanced_math.py. Далее
# создаём в каталоге пустой файл __init__.py. Пакет mathematical готов.
# В Python любая директория с файлом __init__.py автоматически становится
# пакетом. При этом полезный функционал содержится в других питоновских файлах,
# а не в “инит”.

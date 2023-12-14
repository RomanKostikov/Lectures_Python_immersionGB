# Работа с каталогами
# ● Создание каталогов
# Представленный код создаёт каталог в текущей директории. А если необходимо
# создать несколько вложенных друг в друга каталогов, код будет следующим:
import os
from pathlib import Path
# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
# Модуль os предоставляет другую функцию — makedirs. Модуль path работает с тем
# же методом mkdir. Но если в цепочке каталогов будет несуществующий, получим
# ошибку FileNotFoundError. Дополнительный параметр parents=True указывает на
# необходимость создать всех недостающих родительских каталогов.

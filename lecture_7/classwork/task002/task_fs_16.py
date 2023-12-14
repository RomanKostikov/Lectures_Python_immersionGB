# Работа с файлами
# ● Удаление файлов
# Если же необходимо удалить один файл, можно воспользоваться следующими
# вариантами:
import os
from pathlib import Path

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
# И функция remove и метод unlink пытаются удалить файл по указанному пути

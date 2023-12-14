# Работа с каталогами
# ● Удаление каталогов
# Для удаления одного каталога подойдут следующие функция и метод
import os
from pathlib import Path

# os.rmdir('dir')  # OSError
# Path('some_dir').rmdir()  # OSError
os.rmdir('some_dir/dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()
# 🔥 Важно! Удалить можно лишь пустой каталог. Если внутри удаляемого
# каталога есть другие каталоги или файлы, возникнет ошибка OSError.
# Обратите внимание, что при передаче цепочки каталогов удаляется один,
# последний из перечисленных. Родительские каталоги остаются без изменений.

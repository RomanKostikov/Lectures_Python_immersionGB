# Перед вами несколько строчек кода. Какие каталоги и файлы будут созданы после
# его выполнения? У вас три минуты.
import os
import shutil
from pathlib import Path

for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!')
os.mkdir('new_dir')
for i in range(2, 10, 2):
    f = Path(f'file_{i}.txt')
    f.replace('new_dir' / f)
shutil.copytree('new_dir', Path.cwd() / 'dir_new')

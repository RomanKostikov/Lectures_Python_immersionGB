# Подготовка теста и сворачивание работ
# ➢ Метод tearDown
# Метод tearDown будет вызван после успешного выполнения метода setUp и в случае
# если тест отработал успешно, и если он провалился.
import unittest


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()


if __name__ == '__main__':
    unittest.main()
# В примере метод setUp создаёт перед каждым тестом файл со строками чисел. Два
# теста работают с этим файлом. И после каждого происходит удаление файла из
# tearDown метода.
# Даже если провалить тест, файл будет удалён.

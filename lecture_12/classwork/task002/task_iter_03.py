# 2. Создаём итераторы
# Возврат очередного значения, __next__
# Как вы помните из лекции об итераторах и генераторах, любая итерация
# представляет из себя последовательный вызов функции next() с итератором в
# качестве аргумента.
# Для возврата такого значения необходимо определить дандер метод __next__.
class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first < self.stop:
                return self.first

        raise StopIteration


fib = Fibonacci(20, 100)
for num in fib:
    print(num)
# Итератор отработал как и ожидалось.
# ➢ дандер __next__ создаёт цикл пока число в first не превысит значение stop
# ➢ получаем следующую пару Фибоначчи в first и second
# ➢ если first оказывается внутри диапазона [start, stop), возвращаем очередной
# элемент
# ➢ обязательным условием для завершения итерации является вызов ошибки
# StopIteration. Python обрабатывает её как сигнал для завершения итерации и
# перехода к следующему за циклом коду. Остановки кода по ошибке не будет.

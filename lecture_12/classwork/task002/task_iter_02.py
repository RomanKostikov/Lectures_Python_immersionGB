# 2. Создаём итераторы
# Возврат итератора, __iter__
# Для того, чтобы объект стал итерируемым, ему необходимо вернуть
# объект-итератор. В нашем случае экземпляр класса и есть объект-итератор.
# Следовательно он должен вернуть сам себя. Для возврата итератора нужно создать
# дандер метод __iter__.
class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self


fib = Fibonacci(20, 100)
for num in fib:  # TypeError: iter() returned non-iterator of type 'Fibonacci'
    print(num)
# Две строки метода вернули ссылку на самого себя. В результате получаем новую
# ошибку. Вернулся не итерируемый объект

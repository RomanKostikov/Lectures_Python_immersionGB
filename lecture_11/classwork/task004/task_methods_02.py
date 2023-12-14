# 4. Математика и логика в классах
# Сдвиг вправо, __rshift__
# Переопределение методов не обязательно должно быть для чисел. Напишем класс,
# который генерирует шкаф с одеждой и выбрасывает указанное количество вещей
# при правом сдвиге. Не забудем, что дандер метод должен возвращать новый
# экземпляр.
from random import choices


class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка',
               'перчатки', 'носки', 'туфли')

    def __init__(self, count: int, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'Осталось вещей в шкафу {self.count}:\n{names}'

    def __rshift__(self, other):
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))


storeroom = Closet(10)
print(storeroom)
for _ in range(4):
    storeroom = storeroom >> 3
    print(storeroom)
# Константа CLOTHES хранит доступный список одежды. Из него будем выбирать
# count предметов. Внутри __rshift__ сделали проверку на оставшееся количество
# вещей, чтобы не выбросить больше, чем уже имеется. Метод возвращает новый
# экземпляр, где count уменьшился на сдвиг, а второй аргумент содержит выборку из
# уже лежащих в шкафу вещей.
# Создав экземпляр на 10 вещей и последовательно удаляем по три предмета в
# цикле. Но уйти в минус не удаётся, отрабатывает наша защита.

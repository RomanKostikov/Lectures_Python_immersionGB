# 3. Наследование
# MRO
# Попробуем описать классу A дополнительный метод
class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Текст')
        print(self.data_b)


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')
z = Z()
z.say()
a = A()
a.say()  # AttributeError: 'Z' object has no attribute 'data_b'

# Вызов метода say из класса A отработал без ошибок. Мы нашли его двигаясь по
# цепочке линеаризации. При этом метод даже смог обратиться к свойству другого
# класса. Связано это с тем, что мы работаем из экземпляра класса Z и он собрал в
# себя аргументы и методы наследуемых классов.
# 🔥 Важно! Не стоит из родительских классов обращаться к аргументам и
# методам дочерних классов или классов того же уровня наследования.

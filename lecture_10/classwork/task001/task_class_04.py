# 1. Основы ООП в Python
# Экземпляры класса
# Для создания экземпляра класса необходимо выполнить операцию присваивания
# вызвав класс. Точно так же как в примере со списком list.
class Person:
    max_up = 3

p1 = Person()
print(p1.max_up)
# Теперь переменная p1 является экземпляром класса Person. Мы можем обращаться
# в переменным класса из экземпляра.
# Обычно в литературе приводят сравнение класса с чертежом, а его экземпляра с
# объектом, созданным на основе чертежа. Для Python так же будет верно сравнение
# класса с прототипом, а экземпляра с серийным объектом, созданном на основе
# прототипа. Класс — такой же объект, как и экземпляр. С ним та
# к же можно взаимодействовать. Это не просто чертёж на бумаге.
print(Person.max_up)


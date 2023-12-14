# Цикл по целым числам, он же
# арифметический цикл, функция range()
num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)

# Варианты функции range()
# range(stop) — перебираем значения от нуля до stop
# исключительно с шагом один

# range(start, stop) — перебираем значения от start
# включительно до stop исключительно с шагом один

# range(start, stop, step) — перебираем значения от
# start включительно до stop исключительно с шагом step.

# count = 10
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)

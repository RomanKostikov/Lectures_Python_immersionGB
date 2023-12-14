# Аннотация типов в функциях
# "Этот код показывает, как использовать аннотации типов в функциях. Сугубо между программистами.
def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res


print(my_func([2, 5.5, 15, 8.0, 13.74]))

def func(a=0.0, /, b=0.0, *, c=0.0):
    """func(a=0.0: int | float, /, b=0.0: int | float, *, c=0.0: int | float) -> : int | float"""
    if a > c:
        return a
    if a < c:
        return c
    return

print(func(c=1, b=2, a=3))

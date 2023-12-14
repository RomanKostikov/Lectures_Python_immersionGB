def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }')

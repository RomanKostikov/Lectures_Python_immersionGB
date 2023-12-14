name = 'Alex'
age = None

### Функция id()
a = 5
print(id(a))
a = "hello world"
print(id(a))
a = 42.0 * 3.141592 / 2.71828
print(id(a))

print(name, age, a, 456, 'text', sep='()', end='#')
print(123, 'text', sep='()', end='#')

res = input('Enter your name: ')
print(res, 'is your name?', res == name)

age = int(input('Enter your age: '))

adult = 18
how_old = adult - age
print(how_old, "осталось до совершеннолетия")

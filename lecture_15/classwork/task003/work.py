# Пара полезных структур данных
from collections import namedtuple

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'], defaults=[5, 5, 5, 5])
d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data(),
}
print(d)

"""05 Распаковка матрицы
Дан двумерный список (матрица).
Создайте новый список, содержащий все элементы матрицы в одном измерении (список).
Данные:
matrix = [[1, 2], [3, 4], [5, 6]]

Пример вывода:
[1, 2, 3, 4, 5, 6]
"""

from collections.abc import Iterable


matrix = [[1, 2], [3, 4], [5, 6]]

flattened = [
    i
    for sublist in matrix 
    for i in sublist
]

print(flattened)



f = [i for i in matrix]

def flatten(m):
    result = []
    for i in m:
        if isinstance(i, Iterable) and not isinstance(i, str):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


print(flatten(matrix))


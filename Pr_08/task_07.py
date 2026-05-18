"""07 Сравнение матриц

Напишите программу, которая
- обрабатывает две квадратные матрицы одинакового размера
- и проверяет, совпадают ли их диагональные элементы.

Данные:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 0, 3],
    [0, 5, 0],
    [7, 0, 9]
]

Пример вывода:
Совпадают ли главные диагонали: True
Совпадают ли побочные диагонали: True
"""

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 0, 3],
    [0, 5, 0],
    [7, 0, 9]
]

main_diagonal_1 = [matrix1[i][i] for i in range(len(matrix1))]

main_diagonal_2 = [matrix2[i][i] for i in range(len(matrix2))]

print("Совпадают ли главные диагонали: ", main_diagonal_1 == main_diagonal_2)

side_diagonal_1 = [matrix1[i][len(matrix1) - i - 1] for i in range(len(matrix1))]

side_diagonal_2 = [matrix2[i][len(matrix2) - i - 1] for i in range(len(matrix2))]

print("Совпадают ли побочные диагонали: ", side_diagonal_1 == side_diagonal_2)

#========================================================================

main_diagonal = [matrix1[i][i] for i in range(len(matrix1)) if matrix1[i][i] != matrix2[i][i]]

print("Совпадают ли главные диагонали: ", not main_diagonal)

side_diagonal = [matrix1[i][len(matrix1) - i - 1] for i in range(len(matrix1)) if matrix1[i][len(matrix1) - i - 1] != matrix2[i][len(matrix2) - i - 1]]

print("Совпадают ли побочные диагонали: ", not side_diagonal)

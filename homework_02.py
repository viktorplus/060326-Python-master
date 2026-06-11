""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""


def sum_digits_tail(lst):
    pass


def sum_digits_non_tail(lst, acc=0):
    pass


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))       # 28
print(sum_digits_non_tail(nested_numbers))   # 28
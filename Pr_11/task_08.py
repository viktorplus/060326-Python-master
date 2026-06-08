""" 8*. Цепочка шифрования строки

Реализуйте функции:
- Преобразуйте все буквы в предложении в верхний регистр.
- Зашифруйте строку, сдвинув символы на 5 элементов вправо.

Переверните строку.
- Реализуйте функцию шифрования, которая последовательно применит каждую из списка переданных функций к переданной строке.

Данные:
sentence = "Functional programming is powerful"
functions = [to_uppercase, shift_encrypt, reverse_string]

Пример вывода:
QZKWJ\\TU%XN%LSNRRFWLTWU%QFSTNYHSZK
"""


from typing import Callable


def to_uppercase(s: str) -> str:
    return s.upper()

def shift_encrypt(s: str, shift: int = 5) -> str:
    result = ""
    for c in s:
        result += chr(ord(c)+shift)
    return result

def reverse_string(s: str) -> str:
    return s[::-1]


def worker(s: str, jobs: list[Callable]) -> str:
    for f in jobs:
        s = f(s)
    return s

sentence = "Functional programming is powerful"
functions = [to_uppercase, shift_encrypt, reverse_string]

print(worker(sentence, functions))


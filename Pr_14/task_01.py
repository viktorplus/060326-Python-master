""" 01. Генератор, аналогичный range()

Создайте генератор custom_range(), который
- повторяет функциональность range(),
- принимая start, stop, step
- и возвращая последовательность чисел.

Данные:
custom_range(2, 10, 2)
Пример вывода:
2 4 6 8

Данные:
custom_range(10, 0, -3)
Пример вывода:
10 7 4 1
"""

def custom_range(start, stop=None, step=1):
    # Если передано только одно значение — это stop
    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError("step must not be zero")

    # Движение вперёд (step > 0)
    while start < stop:
        yield start
        start += step

    # Движение назад (step < 0)
    while start > stop:
        yield start
        start += step



for num in custom_range(2, 10, 2):
    print(num, end=" ")

# 2 4 6 8

print("\n==============================")

for num in custom_range(10, 0, -3):
    print(num, end=" ")

# 10 7 4 1

""" 11 Уникальные в множестве

Напишите программу, которая
- принимает два множества
- и создаёт список с элементами, которые есть только в одном из множеств.

Решить без использования метода symmetric_difference и оператора ^.
Данные:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

Пример вывода:
[1, 2, 4, 5]
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# --- variant 1 ---
result = []

for item in set1:
    if item not in set2:
        result.append(item)

for item in set2:
    if item not in set1:
        result.append(item)

print(result)

# --- variant 2 ---

result = [item for item in set1 if item not in set2]

result += [item for item in set2 if item not in set1]

print(result)

# --- variant 3 ---

result = list((set1 - set2) | (set2 - set1))

print(result)



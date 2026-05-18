"""04 Группы слов

Напишите программу, которая
- принимает список строк
- и группирует их по общей длине в обратном порядке.

Группы должны быть отсортированы по убыванию длины строки,
а внутри каждой группы строки должны быть отсортированы в алфавитном порядке.

Данные:
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

Пример вывода:
Группы слов:
[['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi', 'pear']]
"""

words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

lenghts = sorted(set(len(w) for w in words), reverse=True)

result = []

for l in lenghts:
    result.append(sorted([w for w in words if len(w) == l]))

print(result)

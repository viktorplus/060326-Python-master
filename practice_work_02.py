""" 02 2. Проверка на панограмму

Напишите программу, которая проверяет, содержит ли строка все буквы
английского алфавита хотя бы по одному разу (игнорируя регистр и пробелы).

Пример вывода:
Исходная строка: The quick brown fox jumps over the lazy dog
Панограмма? True
"""

text = "The quick brown fox jumps over the lazy dog"

text = text.lower()
is_contained = True

for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in text:
        is_contained = False
        break


print("Исходная строка:", text)
print("Панограмма?", is_contained)

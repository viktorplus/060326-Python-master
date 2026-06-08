""" 2.1. Фильтрация списка строк

Отфильтруйте в новый список только слова, длина которых больше трех символов.
Реализуйте в виде функции.

Данные:
words = ["hi", "Hello", "a", "python", "Ok"]

Пример вывода:
['Hello', 'python']
"""


words = ["hi", "Hello", "a", "python", "Ok"]

def filter_long_words(words: list[str], l: int) -> list[str]:
    return [word for word in words if len(word) > l]

sample = ["Hello", "python"]
result = filter_long_words(words, 3)
print(result)            # ['Hello', 'python']
print(result == sample)  # True

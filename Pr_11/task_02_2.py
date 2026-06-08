"""
2.2. Фильтрация списка строк по длине

Доработайте функцию так, чтобы можно было передавать значение минимальной длины слов, которые нужно оставить.
words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 2

Пример вывода:
['hi', 'Hello', 'python', 'Ok']
"""

words = ["hi", "Hello", "a", "python", "Ok"]

def filter_long_words(words: list[str], min_len: int = 3) -> list[str]:
    return [word for word in words if len(word) >= min_len]

result = filter_long_words(words, 2)

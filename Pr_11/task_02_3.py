""" 2.3. Фильтрация списка строк по критерию

Доработайте функцию так, чтобы можно было передавать критерии отбора слов, которые нужно оставить.
(то есть аргументом должен стать callable-объект)
Например:
- слова, начинаются с заглавной буквы
- слова из одного символа
- слова начинаются и заканчиваются одной буквой, независимо от регистра

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
Пример вывода:
['Hello', 'Ok', 'Radar']
['a']
['a', 'Radar']
"""

from typing import Callable


words = ["hi", "Hello", "a", "python", "Ok"]

def filter_long_words(words: list[str], f: Callable[[str], bool]) -> list[str]:
    return [word for word in words if f(word)]


def starts_with_capital(word: str) -> bool:
    return word[0].isupper()

def has_one_symbol(word: str) -> bool:
    return len(word) == 1

def starts_and_ends_with_letter(word: str) -> bool:
    return word[0].islower() and word[-1].islower()


print(filter_long_words(words, starts_with_capital))
print(filter_long_words(words, has_one_symbol))
print(filter_long_words(words, starts_and_ends_with_letter))

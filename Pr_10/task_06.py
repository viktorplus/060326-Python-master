""" 06 Группировка слов по длине
Реализуйте функцию, которая группирует слова по их длине в и возвращает словарь с ними.
Данные:
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]

Пример вывода:
Слова по длине:
5: ['apple', 'grape', 'peach']
6: ['banana', 'orange']
4: ['kiwi']
"""

from collections import defaultdict
from pprint import pprint


def group_words_by_length(words):
    length = defaultdict(list)

    for word in words:
        length[len(word)].append(word)
        
    return length


words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]

res = group_words_by_length(words)

pprint(res)

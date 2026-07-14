"""
3. Кеширование результатов
Создайте декоратор cache, который сохраняет результат вызова функции
для каждого набора аргументов.
Если функция вызывается повторно с теми же аргументами —
возвращается сохранённый результат.

Пример применения:
@cache
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

Пример вывода:
print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

Вычисляем 2 * 3:
6
Результат из кеша:
6
Вычисляем 4 * 5:
20
Результат из кеша:
6
"""
def cache(func):
    cache = {}
    def wrapper(*args):
        if cache.get(args):

            print(f"Результат из кеша: {cache[args]}")

            return cache[args]

        cache[args] = func(*args)

        return cache[args]

    return wrapper



@cache
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Результат из кеша:
# 6

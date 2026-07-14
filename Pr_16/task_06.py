"""
6. Проверка типов аргументов по порядку

Создайте декоратор accepts_types, который проверяет,
что позиционные аргументы функции соответствуют указанным типам.
Если тип хотя бы одного аргумента не совпадает —
должна быть выброшено исключение TypeError с указанием ожидаемого и полученного типа.

Пример применения:
@accepts_types(int, int)
def add(a, b):
    return a + b

@accepts_types(str)
def greet(name):
    return f"Hello, {name}!"

@accepts_types(str, str)
def greet_by_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

Пример вызова:
try:
    print(add(5, 3))
    print(greet_by_name("Anna"))
    print(add("one", 3))             # ошибка
except Exception as e:
    print(e)
try:
    print(greet_by_name("Anna", 0))  # ошибка
except Exception as e:
    print(e)

Пример вывода:
8
Hello, Anna!
Incorrect type for argument 'one': expected - <class 'int'>, received - <class 'str'>
Incorrect type for argument '0': expected - <class 'str'>, received - <class 'int'>

"""

def accepts_types(*expected_types):
    def wrapper1(func):
        def wrapper2(*args):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Incorrect type for argument '{arg}': expected - {expected_type}, received - {type(arg)}")

            return func(*args)

        return wrapper2

    return wrapper1


@accepts_types(int, int)
def add(a, b):
    return a + b

@accepts_types(str)
def greet(name):
    return f"Hello, {name}!"

@accepts_types(str, str)
def greet_by_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

try:
    print(add(5, 3))
    print(greet_by_name("Anna"))
    print(add("one", 3))             # ошибка
except Exception as e:
    print(e)
try:
    print(greet_by_name("Anna", 0))  # ошибка
except Exception as e:
    print(e)


# 8
# Hello, Anna!
# Incorrect type for argument 'one': expected - <class 'int'>, received - <class 'str'>
# Incorrect type for argument '0': expected - <class 'str'>, received - <class 'int'>

""" 6. Анализ оценок студентов

Дан список студентов с их оценками по разным предметам.
Напишите программу, которая:
- Вычисляет среднюю оценку для каждого студента.
- Возвращает словарь студентов с их средней оценкой, отсортированный по убыванию оценок.

Данные:
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [78, 81, 75]},
    {"name": "Charlie", "grades": [95, 92, 90]},
    {"name": "Diana", "grades": [88, 84, 82]}
]

Пример вывода:
{'Charlie': 92.33, 'Alice': 87.67, 'Diana': 84.67, 'Bob': 78.0}
"""
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [78, 81, 75]},
    {"name": "Charlie", "grades": [95, 92, 90]},
    {"name": "Diana", "grades": [88, 84, 82]}
]

def get_average(g: list[int]) -> float:
    return round(sum(g) / len(g), 2)

def average_by_name1(students: list[dict[str, list[int]]]) -> dict:
    result = {
        s["name"]: get_average(s["grades"])
        for s in students 
    }

    students_sorted = sorted( result.items(), key=lambda x: x[1], reverse=True)

    return dict(students_sorted)




def average_by_name(students: list[dict[str, list[int]]]) -> dict[str, float]:
    result = {}
    for student in students:
        result[student["name"]] = round(sum(student["grades"]) / len(student["grades"]), 2)
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    

print(average_by_name(students))
print(average_by_name1(students))


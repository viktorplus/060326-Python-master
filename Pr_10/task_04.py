""" 04 Очередь задач с приоритетом
Есть очередь задач, где каждая задача имеет приоритет: "высокий", "средний", "низкий".
Реализуйте функцию, которая сортирует очередь задач таким образом, чтобы более высокий приоритет был в начале очереди.
Нужно изменить исходную очередь, а не создавать новую.
Данные:
tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})
Пример вывода:
Очередь задач:
	task3: высокий
	task5: высокий
	task2: средний
	task1: низкий
	task4: низкий
"""
from collections import OrderedDict

tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})


sort_map = ["высокий", "средний", "низкий"]

def sort_by_priority(tasks):
    for value in sort_map:
        for task, priority in tasks.copy().items():
            if priority == value:
                tasks.move_to_end(task)


sort_by_priority(tasks)

print("Очередь задач:")

for task, priority in tasks.items():
    print(f"\ttask{task}: {priority}")


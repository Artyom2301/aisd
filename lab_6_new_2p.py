# 2 часть – написать программу в соответствии со своим вариантом задания.
# Усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)...
# ...и целевую функцию для нахождения оптимального  решения.
# Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
# Вариант 17. В группе N человек. Сформировать все возможные варианты разбиения группы на подгруппы  при условии, что в подгруппу входит не более 10 человек.
# Ограничение: суммарная зарплата подгруппы не должна превышать заданного бюджета 
# Целевая функция: выбрать подгруппу с максимальной общей зарплатой, но при этом не выходящую за рамки бюджета 

import time
from itertools import combinations
import random

N = int(input("Введите количество человек в группе: "))
MAX_GROUP = 10
BUDGET = int(input("Введите бюджет подгруппы: "))

# Генерируем зарплаты участников
salaries = [random.randint(50, 200) for _ in range(N)]
print("Зарплаты участников:", salaries)

# -------- Ограничение --------
def check_group(group):
    """Проверяем, не превышает ли подгруппа бюджет"""
    total_salary = sum(salaries[i] for i in group)
    return total_salary <= BUDGET

# -------- Целевая функция --------
def group_value(group):
    """Целевая функция – суммарная зарплата подгруппы"""
    return sum(salaries[i] for i in group)

# ------------------------------------
# ВАРИАНТ 1. АЛГОРИТМИЧЕСКИЙ
# ------------------------------------
print("\nАлгоритмический подход:")
start_time = time.time()

best_group = None
best_value = 0

for size in range(1, min(MAX_GROUP, N) + 1):
    # вручную формируем комбинации
    subgroup = list(range(size))
    while True:
        if check_group(subgroup):
            val = group_value(subgroup)
            if val > best_value:
                best_value = val
                best_group = subgroup.copy()

        # сдвиг комбинации
        for i in reversed(range(size)):
            if subgroup[i] != N - size + i:
                break
        else:
            break

        subgroup[i] += 1
        for j in range(i + 1, size):
            subgroup[j] = subgroup[j - 1] + 1

end_time = time.time()
print("Лучшая подгруппа:", [x+1 for x in best_group] if best_group else None)
print("Её суммарная зарплата:", best_value)
print("Время выполнения алгоритмического варианта:", end_time - start_time, "сек.")

# ------------------------------------
# ВАРИАНТ 2. С ПОМОЩЬЮ ФУНКЦИЙ PYTHON
# ------------------------------------
print("\nФункциональный подход:")
start_time = time.time()

best_group_f = None
best_value_f = 0

for size in range(1, min(MAX_GROUP, N) + 1):
    for group in combinations(range(N), size):
        if check_group(group):
            val = group_value(group)
            if val > best_value_f:
                best_value_f = val
                best_group_f = group

end_time = time.time()
print("Лучшая подгруппа:", [x+1 for x in best_group_f] if best_group_f else None)
print("Её суммарная зарплата:", best_value_f)
print("Время выполнения функционального варианта:", end_time - start_time, "сек.")

#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
#В группе N человек. Сформировать все возможные варианты разбиения группы на подгруппы  при условии, что в подгруппу входит не более 10 человек.
import time
from itertools import combinations
import more_itertools

# ---------- ПАРАМЕТРЫ ----------
N = 12
MAX_GROUP_SIZE = 10
group = list(range(1, N + 1))

# ---------- ЧАСТЬ 1 ----------
# Алгоритмический способ (рекурсия)
def split_recursive(group, max_size):
    if not group:
        return [[]]
    
    result = []
    n = len(group)
    for size in range(1, min(max_size, n) + 1):
        for subset in combinations(group, size):
            rest = list(set(group) - set(subset))
            for partition in split_recursive(rest, max_size):
                result.append([list(subset)] + partition)
    return result

# Встроенные функции Python (через more_itertools)
def valid_partitions(group, max_size):
    all_partitions = more_itertools.set_partitions(group)
    return [p for p in all_partitions if all(len(part) <= max_size for part in p)]

# --- Запуск первой реализации ---
start_time = time.time()
partitions_1 = split_recursive(group, MAX_GROUP_SIZE)
time_1 = time.time() - start_time
print(f"Алгоритмический способ: {len(partitions_1)} вариантов за {time_1:.3f} сек.")

# --- Запуск второй реализации ---
start_time = time.time()
partitions_2 = valid_partitions(group, MAX_GROUP_SIZE)
time_2 = time.time() - start_time
print(f"С использованием библиотеки: {len(partitions_2)} вариантов за {time_2:.3f} сек.")


# ---------- ЧАСТЬ 2 ----------
# Ограничение: участники, которые не могут быть вместе
conflicts = {(3, 5), (2, 4)}

def is_valid_group(group):
    for a, b in conflicts:
        if a in group and b in group:
            return False
    return True

def is_valid_partition(partition):
    return all(is_valid_group(group) for group in partition)

# Целевая функция: минимизировать разницу между размерами групп
def objective_function(partition):
    sizes = [len(group) for group in partition]
    return - (max(sizes) - min(sizes))  # Чем меньше разница, тем лучше

# Фильтруем по ограничениям и сортируем по целевой функции
valid_and_optimized = [p for p in partitions_2 if is_valid_partition(p)]
valid_and_optimized.sort(key=objective_function, reverse=True)

# Выводим лучшее разбиение
if valid_and_optimized:
    best_partition = valid_and_optimized[0]
    print("\n Лучшая комбинация с учётом ограничений и целевой функции:")
    for i, subgroup in enumerate(best_partition, 1):
        print(f"  Группа {i}: {subgroup}")
else:
    print("Нет подходящих разбиений с учётом ограничений.")

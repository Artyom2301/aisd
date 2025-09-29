# 1 часть – написать программу в соответствии со своим вариантом задания.
# Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
# Вариант 17. В группе N человек. Сформировать все возможные варианты разбиения группы на подгруппы  при условии, что в подгруппу входит не более 10 человек.
import time
from itertools import combinations

N = int(input("Введите количество человек: "))   # размер группы
MAX_GROUP = 10                                   # максимальный размер подгруппы

# -------------------------------------
# Вариант 1. Алгоритмический
# -------------------------------------
print("Алгоритмический подход:")
start_time = time.time()

if N == 0:
    print("Группа пуста.")
else:
    # Формируем все подгруппы размером от 1 до MAX_GROUP
    for size in range(1, min(MAX_GROUP, N) + 1):
        # создаём подгруппы вручную
        subgroup = list(range(size))
        while True:
            # выводим текущую подгруппу (нумерация с 1)
            print([x + 1 for x in subgroup])

            # находим позицию для сдвига
            for i in reversed(range(size)):
                if subgroup[i] != N - size + i:
                    break
            else:
                # дошли до последней комбинации
                break

            subgroup[i] += 1
            for j in range(i + 1, size):
                subgroup[j] = subgroup[j - 1] + 1

end_time = time.time()
print("Время выполнения алгоритмического варианта:", end_time - start_time)

# -------------------------------------
# Вариант 2. С помощью функций Python
# -------------------------------------
print("\nФункциональный подход:")
start_time = time.time()

if N == 0:
    print("Группа пуста.")
else:
    people = list(range(1, N + 1))
    for size in range(1, min(MAX_GROUP, N) + 1):
        for subgroup in combinations(people, size):
            print(list(subgroup))

end_time = time.time()
print("Время выполнения функционального варианта:", end_time - start_time)
 

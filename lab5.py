import time
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Устанавливаем высокую точность для Decimal
getcontext().prec = 1000

# Кэш для факториалов
factorials = {}

def factorial(n):
    if n not in factorials:
        result = Decimal(1)
        for i in range(1, n + 1):
            result *= i
        factorials[n] = result
    return factorials[n]

# Рекурсивная реализация с Decimal
def recursive_F(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return Decimal(1)
    result = Decimal((-1)**n) * (
        recursive_F(n - 1) / factorial(n) - recursive_F(n - 2) / factorial(2 * n)
    )
    cache[n] = result
    return result

# Итеративная реализация с Decimal
def iterative_F(n):
    f = [Decimal(1), Decimal(1)]  # F(0), F(1)
    for i in range(2, n + 1):
        term1 = f[i - 1] / factorial(i)
        term2 = f[i - 2] / factorial(2 * i)
        val = Decimal((-1)**i) * (term1 - term2)
        f.append(val)
    return f[n]

# Ввод с проверкой
n = int(input('Введите натуральное число (n ≥ 2): '))
while n < 2:
    n = int(input('Попробуй ещё раз, число должно быть ≥ 2: '))

# Сравнение времени выполнения
start_time = time.time()
recursive_result = recursive_F(n)
recursive_time = time.time() - start_time

start_time = time.time()
iterative_result = iterative_F(n)
iterative_time = time.time() - start_time

print(f"Рекурсивно: F({n}) = {recursive_result}, время: {recursive_time:.6f} секунд")
print(f"Итеративно: F({n}) = {iterative_result}, время: {iterative_time:.6f} секунд")

# Построение графика времени
graf = list(range(2, n + 1))
timer_rec = []
timer_iter = []

for i in graf:
    start = time.time()
    recursive_F(i)
    timer_rec.append(time.time() - start)

    start = time.time()
    iterative_F(i)
    timer_iter.append(time.time() - start)

plt.plot(graf, timer_iter, label='Итеративная функция')
plt.plot(graf, timer_rec, label='Рекурсивная функция')
plt.xlabel('Значение n')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение времени работы функций')
plt.legend()
plt.grid(True)
plt.show()


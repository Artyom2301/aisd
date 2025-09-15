# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц B,C,D,E...
# ...заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
# Вариант 17
# Формируется матрица F следующим образом: если в Е количество нулей в нечетных столбцах в области 4 больше, чем...
# ...сумма чисел в нечетных строках в области 1, то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: (К*(A*F)– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
import random
from math import ceil

# Ввод размерности матрицы и значения K
N = int(input("Введите размерность матрицы: "))
K = int(input("Введите значение K: "))
middle_n = N // 2 + N % 2 # Середина матрицы
sum_ = 0 # Сумма чисел в подматрице E в области 1 в нечётных строках
num_zero = 0 # Количество нулей в подматрице E в области 4 в нечётных столбцах

# Генерация случайной матрицы A
def generate_matrix(N):
  matrix=[]
  for i in range(N):
    pr_a = []
    for j in range(N):
        pr_a.append(random.randint(-10, 10))
    matrix.append(pr_a)
  return matrix


# Вывод матрицы A
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{el:4}" for el in row))
A = []
with open("matrix.txt", "r") as f:
    for line in f:
        row = list(map(int, line.split()))  # превращаем строку в список чисел
        A.append(row)
print("Матрица A:")
print_matrix(A)

AT = [[0 for i in range(N)] for j in range(N)]  # Транспонированная матрица А
F = A.copy()  # Задаём матрицу F
AF = [[0 for i in range(N)] for j in range(N)]  # Результат умножения матрицы A на матрицу F
KAF = [[0 for i in range(N)] for j in range(N)]  # Результат умножения матрицы AF на коэффициент K
KAT = [[0 for i in range(N)] for j in range(N)]  # Результат умножения матрицы AT на коэффициент K
rez = [[0 for i in range(N)] for j in range(N)] # Результат вычитания матриц

# Транспонируем матрицу А
for i in range(N):
    for j in range(N):
        AT[i][j] = A[j][i]

# Разбиваем матрицу А на 4 равных подматрицы
if N % 2 == 1:
    E = [A[i][middle_n - 1:N] for i in range(middle_n)]
    C = [A[i][0:middle_n] for i in range(middle_n - 1, N)]
    B = [A[i][middle_n - 1:N] for i in range(middle_n - 1, N)]
    D = [A[i][0:middle_n] for i in range(middle_n)]
else:
    E = [A[i][middle_n:N] for i in range(0, middle_n)]
    C = [A[i][0:middle_n] for i in range(middle_n, N)]
    B = [A[i][middle_n:N] for i in range(middle_n, N)]
    D = [A[i][0:middle_n] for i in range(0, middle_n)]

# Количество нулей в подматрице E в области 4 в нечётных столбцах
for i in range(middle_n):
    for j in range(1,middle_n):
        if (i < j) and i < ((middle_n - 1 - j)) and (j % 2 != 0):
            if E[i][j] == 0:
                num_zero += 1
# Вычисление суммы чисел в подматрице E в области 1 в нечётных строках
for i in range(1,middle_n):
    for j in range(middle_n):
        if (i < j) and i > ((middle_n - 1 - j)) and (i % 2 != 0):
            sum_ += E[i][j]

# Замена областей 1 и 2 симметрично в подматрице E
if num_zero > sum_:
    print(f'\nВ подматрице "E" количество нулей в нечётных столбцах в области 4({num_zero})')
    print(f'больше чем сумма чисел в нечётных строках в области 1({sum_})')
    print('поэтому симметрично меняем местами области 1 и 2 в подматрице E.')
    for i in range(middle_n-1,ceil(middle_n / 2)-1,-1):
        for j in range(i+1):
            E[i][j], E[j][i] = E[j][i], E[i][j]
    if N % 2 == 1:
        for i in range(middle_n):
            for j in range(middle_n - 1, N):
                F[i][j] = E[i][j - (middle_n - 1)]  # Перезаписываем E
    else:
        for i in range(0, middle_n):
            for j in range(middle_n, N):
                F[i][j] = E[i][j - middle_n]

# Замена подматриц С и E несимметрично
else:
    print(f'\nВ подматрице "E" количество нулей в нечётных столбцах в области 4({num_zero})')
    print(f'меньше чем сумма чисел в нечётных строках в области 1({sum_}) или равна ей')
    print('поэтому несимметрично меняем местами подматрицы C и E:')
    C, E = E, C
    if N % 2 == 1:
        for i in range(middle_n - 1, N):  # Перезаписываем C
            for j in range(middle_n - 1, N):
                F[i][j] = C[i - (middle_n - 1)][j - (middle_n - 1)]
        for i in range(middle_n):  # Перезаписываем Е
            for j in range(middle_n - 1, N):
                F[i][j] = E[i][j - (middle_n - 1)]
    else:
        for i in range(middle_n, N):
            for j in range(middle_n, N):
                F[i][j] = C[i - middle_n][j - middle_n]  # Перезаписываем C
        for i in range(0, middle_n):
            for j in range(middle_n, N):
                F[i][j] = E[i][j - middle_n]  # Перезаписываем Е

# K * AT
for i in range(N):
    for j in range(N):
        KAT[i][j] = K * AT[i][j]

# A * F
for i in range(N):
    for j in range(N):
        for o in range(N):
            AF[i][j] += A[i][o] * F[o][j]

# K * AF
for i in range(N):
    for j in range(N):
        KAF[i][j] = K * AF[i][j]

# KFA - KAT
for i in range(N):
    for j in range(N):
        rez[i][j] = KAF[i][j] - KAT[i][j]

# Вывод всех операций и полученной матрицы
print("Матрица AT:")
print_matrix(AT)

print("Матрица F:")
print_matrix(F)

print("Результат K * AT:")
print_matrix(KAT)

print("Результат A * F:")
print_matrix(AF)

print("Результат K * AF:")
print_matrix(KAF)

print("Результат К * (F * А) – K * AT:")
print_matrix(rez)




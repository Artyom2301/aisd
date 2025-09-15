# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц B,C,D,E...
# ...заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
# Вариант 17
# Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах больше, чем...
# ...сумма чисел в нечетных строках, то поменять местами В и Е симметрично, иначе С и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,то вычисляется выражение:A^-1 * AT – K * F^-1, иначе...
# ...вычисляется выражение (A^-1 + G - F^-1) * K, где G-нижняя треугольная матрица, полученная из А.
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import numpy as np
import matplotlib.pyplot as plt

# Ввод размерности матрицы и значения K
#N = int(input("Введите размерность матрицы: "))
K = int(input("Введите значение K: "))
with open("matrix.txt", "r") as f:
    first_line = f.readline()         # читаем первую строку
    numbers = first_line.split()      # делим по пробелам
    N = len(numbers)

middle_n = N // 2 + N % 2 # Середина матрицы
A = []
with open("matrix.txt", "r") as f:
    for line in f:
        row = list(map(int, line.split()))  # превращаем строку в список чисел
        A.append(row)
#A = np.random.randint(-10, 10, (N, N)) # Генерация матрицы A
AT = np.transpose(A) # Транспонированная матрица А
det_A = np.linalg.det(A) # Определитель матрицы А
A_1 = np.linalg.inv(A) # Обратная матрица А
F = A.copy() # Задаём матрицу F
G = np.tri(N) * A # Матрица G

num_zero = 0 # Количество нулей в подматрице E в нечётных столбцах
sum_ = 0 # Сумма чисел в подматрице E в нечётных строках
sum_ele_F = 0 # Сумма диагональных элементов матрицы F
# Вывод матрицы А
print(f'\nМатрица А:\n{A}')

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

# Количество нулей в подматрице E в нечётных столбцах
for i in range(middle_n):
    for j in range(1,middle_n):
        if j % 2 != 0:
            if E[i][j] == 0:
                num_zero += 1

# Вычисление суммы чисел в подматрице E в нечётных строках
for i in range(1,middle_n):
    for j in range(middle_n):
        if i % 2 != 0:
            sum_ += E[i][j]

# Замена В и Е симметрично
if num_zero > sum_:
    print(f'\nВ подматрице "E" количество нулей в нечётных столбцах ({num_zero})')
    print(f'больше чем сумма чисел в нечётных строках ({sum_})')
    print('поэтому симметрично меняем местами подматрицы B и E.')
    B, E = E, B
    for i in range(middle_n):
        B[i] = B[i][::-1]  # Симметрично меняем значения в B
        E[i] = E[i][::-1]  # Симметрично меняем значения в E
    if N % 2 == 1:
        for i in range(middle_n - 1, N):
            for j in range(middle_n):
                F[i][j] = B[i - (middle_n - 1)][j]  # Перезаписываем B
        for i in range(middle_n):
            for j in range(middle_n - 1, N):
                F[i][j] = E[i][j - (middle_n - 1)]  # Перезаписываем Е
    else:
        for i in range(middle_n, N):
            for j in range(middle_n):
                F[i][j] = B[i - middle_n][j]  # Перезаписываем B
        for i in range(0, middle_n):
            for j in range(middle_n, N):
                F[i][j] = E[i][j - middle_n]  # Перезаписываем Е

# Замена подматриц С и E несимметрично
else:
    print(f'\nВ матрице "В" количество строк с нулями на чётных позициях({num_zero})')
    print(f'меньше чем сумма положительных элементов в чётных строках({sum_}) или равно ей')
    print('поэтому несимметрично меняем местами подматрицы B и E:')
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
# Вывод матрицы F
print(f'\nМатрица F:\n{F}')

# Сумма диагональных элементов матрицы F
for i in range(N):
    for j in range(N):
        if i == j:
            sum_ele_F += F[i][j]

# Вычисление выражения: A^-1 * AT – K * F^-1
if det_A > sum_ele_F:
    print(f'\nОпределитель матрицы А ({int(det_A)})')
    print(f'больше,чем сумма диагональных элементов матрицы F({int(sum_ele_F)})')
    print('поэтому вычисляем выражение:A^-1 * AT – K * F^-1 :')
    F_1 = np.linalg.inv(F) # Обратная матрица F
    KF_1 = K * F_1 # K * F^-1
    A_1AT = A_1 * AT # A^-1 * AT
    rez = A_1AT - KF_1 # A^-1 * AT – K * F^-1

    # Вывод всех операций
    print(f'\nОбратная матрица F:\n{F_1}')
    print(f'\nРезультат K * F^-1:\n{KF_1}')
    print(f'\nРезультат A^-1 * AT:\n{A_1AT}')
    print(f'\nРезультат A^-1 * AT – K * F^-1 :\n{rez}')

# Вычисление выражения: (A^-1 + G - F^-1) * K
else:
    print(f'\nОпределитель матрицы А ({int(det_A)})')
    print(f'меньше,чем сумма диагональных элементов матрицы F({int(sum_ele_F)}) или равен ей')
    print('поэтому вычисляем выражение: (A^-1 + G - F^-1)*K:')
    F_1 = np.linalg.inv(F) # Обратная матрица F
    GF_1 = G - F_1 # G - F^-1
    A_1GF_1 = A_1 + GF_1 # A^-1 + G - F^-1
    rez = A_1GF_1 * K # (A^-1 + G - F^-1) * K

    # Вывод всех операций
    print(f'\nОбратная матрица F:\n{F_1}')
    print(f'\nРезультат G - F^-1:\n{GF_1}')
    print(f'\nРезультат A^-1 + G - F^-1:\n{A_1GF_1}')
    print(f'\nРезультат (A^-1 + G - F^-1) * K:\n{rez}')

# Построение графиков
plt.title("Высота столбца от числа элемента второй строки")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.bar(range(0,N),F[1],color='blue',alpha=0.9) # Столбчатая диаграмма
plt.show()

plt.title("Зависимость y = sin от элементов F, x = соs от элементов F")
plt.plot(np.cos(F),np.sin(F),linestyle="-",color="blue") # Линейный график
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

plt.title("Визуализация матрицы F через график ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
n, bin, patches = plt.hist(F, bins=20) # Гистограмма
plt.show()

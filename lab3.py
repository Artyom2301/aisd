import random

def print_matrix(M, name=""):
    if name:
        print(f"\nМатрица {name}:")
    for row in M:
        print(" ".join(f"{el:4}" for el in row))

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def multiply(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def scale_matrix(M, K):
    return [[el * K for el in row] for row in M]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def get_area(i, j, size):
    if i < j and i + j < size - 1:
        return 4
    elif i < j and i + j > size - 1:
        return 3
    elif i > j and i + j > size - 1:
        return 2
    elif i > j and i + j < size - 1:
        return 1
    else:
        return 0

def count_zeros_area4_odd_cols(E):
    size = len(E)
    count = 0
    for i in range(size):
        for j in range(size):
            if get_area(i, j, size) == 4 and j % 2 == 1 and E[i][j] == 0:
                count += 1
    return count

def sum_area1_odd_rows(E):
    size = len(E)
    total = 0
    for i in range(size):
        for j in range(size):
            if get_area(i, j, size) == 1 and i % 2 == 1:
                total += E[i][j]
    return total

def swap_symmetric_areas(E):
    size = len(E)
    for i in range(size):
        for j in range(size):
            if get_area(i, j, size) == 1:
                x, y = j, i
                if get_area(x, y, size) == 2:
                    E[i][j], E[x][y] = E[x][y], E[i][j]
    return E

def input_int(prompt, condition=lambda x: True):
    while True:
        try:
            x = int(input(prompt))
            if condition(x):
                return x
        except:
            pass
        print("Неверный ввод. Попробуйте снова.")

def main():
    N = input_int("Введите чётное N > 4: ", lambda x: x > 4 and x % 2 == 0)
    K = input_int("Введите коэффициент K: ")

    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
    print_matrix(A, "A")

    half = N // 2
    B = [row[:half] for row in A[:half]]
    C = [row[half:] for row in A[:half]]
    D = [row[:half] for row in A[half:]]
    E = [row[half:] for row in A[half:]]

    print_matrix(B, "B")
    print_matrix(C, "C")
    print_matrix(D, "D")
    print_matrix(E, "E (до изменений)")

    # Анализ областей
    zeros_area4 = count_zeros_area4_odd_cols(E)
    sum_area1 = sum_area1_odd_rows(E)

    print(f"\nНулей в нечётных столбцах области 4: {zeros_area4}")
    print(f"Сумма в нечётных строках области 1: {sum_area1}")

    if zeros_area4 > sum_area1:
        print("Условие выполнено: меняем области 1 и 2 в E симметрично.")
        E = swap_symmetric_areas(E)
    else:
        print("Условие НЕ выполнено: меняем C и E несимметрично.")
        C, E = E, C

    # Формируем F из B, C, D, E
    F = []
    for i in range(half):
        F.append(B[i] + C[i])
    for i in range(half):
        F.append(D[i] + E[i])

    print_matrix(F, "F")

    AF = multiply(A, F)
    print_matrix(AF, "A * F")

    KAF = scale_matrix(AF, K)
    print_matrix(KAF, "K * (A * F)")

    AT = transpose(A)
    print_matrix(AT, "A^T")

    KAT = scale_matrix(AT, K)
    print_matrix(KAT, "K * A^T")

    result = subtract_matrices(KAF, KAT)
    print_matrix(result, "Результат (K*(A*F) – K*A^T)")

if __name__ == "__main__":
    main()

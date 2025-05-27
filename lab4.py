import matplotlib.pyplot as plt
import numpy as np

def fill_matrix(matrix, submatrix):
    half_size = len(matrix) // 2
    for i, key in enumerate(['D', 'E', 'C', 'B']):
        row_start = half_size * (i // 2)
        col_start = half_size * (i % 2)
        matrix[row_start:row_start+half_size, col_start:col_start+half_size] = submatrix[key]

def main():
    N = int(input("Введите размерность матрицы N (четное число): "))
    if N % 2 != 0:
        raise ValueError("Размерность должна быть чётной")
    K = int(input("Введите коэффициент K: "))

    submatrix = {'D': [], 'E': [], 'C': [], 'B': []}
    A = np.zeros((N, N), dtype=np.int64)
    F = np.zeros((N, N), dtype=np.int64)

    for key in submatrix:
        submatrix[key] = np.random.randint(-10, 11, size=(N//2, N//2))
        print(f'Подматрица {key}:\n{submatrix[key]}\n')

    fill_matrix(A, submatrix)
    print('Матрица A:\n', A)

    # Работаем с подматрицей E
    E = submatrix['E']
    count_zeros = np.sum(E[:, ::2] == 0)  # Нули в нечетных столбцах (0, 2, ...)
    sum_odd_rows = np.sum(E[1::2])        # Сумма чисел в нечетных строках (1, 3, ...)

    print(f'Количество нулей в нечётных столбцах E: {count_zeros}')
    print(f'Сумма элементов в нечётных строках E: {sum_odd_rows}')

    if count_zeros > sum_odd_rows:
        # Симметрично меняем B и E (по горизонтали)
        submatrix['B'] = np.fliplr(submatrix['E'])
        submatrix['E'] = np.fliplr(submatrix['B'])
        print('Симметричный обмен B и E:')
    else:
        # НЕсимметрично меняем C и E
        submatrix['C'], submatrix['E'] = submatrix['E'], submatrix['C']
        print('НЕсимметричный обмен C и E:')

    print('Подматрица B:\n', submatrix['B'])
    print('Подматрица C:\n', submatrix['C'])
    print('Подматрица E:\n', submatrix['E'])

    fill_matrix(F, submatrix)
    print('\nМатрица F:\n', F)

    # Определитель A
    det_A = round(np.linalg.det(A), 3)
    print(f'\nОпределитель матрицы A: {det_A}')

    # Сумма диагональных элементов F
    diag_sum_F = np.trace(F)
    print(f'Сумма диагональных элементов матрицы F: {diag_sum_F}')

    if det_A > diag_sum_F:
        A_inv = np.linalg.inv(A)
        F_inv = np.linalg.pinv(F)
        AT = A.T
        result = np.dot(A_inv, AT) - K * F_inv
        print('\nВычисляется выражение: A⁻¹ * Aᵗ – K * F⁻¹')
    else:
        A_inv = np.linalg.inv(A)
        G = np.tril(A)
        F_inv = np.linalg.pinv(F)
        result = (A_inv + G - F_inv) * K
        print('\nВычисляется выражение: (A⁻¹ + G - F⁻¹) * K')

    result = np.round(result, 3)
    print('\nРезультат выражения:\n', result)

    # Графики
    plt.figure(figsize=(18, 4))

    plt.subplot(1, 4, 1)
    plt.hist(F.flatten(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Гистограмма матрицы F')

    plt.subplot(1, 4, 2)
    labels = ['B', 'C', 'D', 'E']
    sizes = [np.sum(submatrix[key]) for key in labels]
    sizes = [max(0, s) + 0.01 for s in sizes]  # чтобы не было деления на 0
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Круговая диаграмма подматриц')

    plt.subplot(1, 4, 3)
    plt.plot(np.diag(F), marker='o', color='green')
    plt.title('Линейный график главной диагонали F')

    plt.subplot(1, 4, 4)
    plt.bar(np.arange(len(sizes)), sizes, color='orange')
    plt.xticks(np.arange(len(labels)), labels)
    plt.title('Гистограмма суммы элементов подматриц')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

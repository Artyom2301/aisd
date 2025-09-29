# Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.

# Вариант 17
# 17.	F(0) = 1, F(1) = 1, F(n) = (-1)n*(F(n–1)/n! - F(n-2) /(2n)!), при n > 1
import time
import matplotlib.pyplot as plt
from functools import lru_cache
k = 1 # Ответ пользователя
p = 1

# Факториал для рекурсии
def rec_factor(number):
    if number == 1:
        return 1
    else:
        return number * rec_factor(number-1)

# Нахождение F рекурсивно
p = 1
@lru_cache(maxsize=None)
def F_rec(n):
    if n <= 1:
        return 1
    else:
        global p
        p *= -1
        return p * (F_rec(n-1)/rec_factor(n) - F_rec(n - 2)/(rec_factor(2*n)))

# Факториал для итерации
@lru_cache(maxsize=None)
def it_factor(n):
    s = 1
    for i in range(2,n+1):
        s *= i
    return s

# Нахождение F  итерационно
p = 1
def F_iter(n):
    F = [0]*(n+1)
    F[0] = 1
    F[1] = 1
    global p
    for i in range(2, n):
        p *= -1
        F[i] = p * (F_iter(n-1)/it_factor(n) - F_iter(n - 2)/(it_factor(2*n)))        
    return F[n]

# Ввод числа N и S
n = int(input('Введите натуральное число n, для функции F(n): '))
while n < 1:
    n = int(input('Введите число n больше 0. Рассматривается только последовательность натуральных чисел: '))

s = int(input('\nВведите натуральное число s, являющееся шагом в сравнительной таблице и графике: '))
while s < 1:
    s = int(input('Введите шаг графика >= 1: '))

# Cписки для нахождения времени
timer=[]
timer_rec=[]
graf = list(range(1, n + 1,s))

# Выбор выполнения программы
o = int(input('\nДля какой функции вы хотите выполнить программу? '
                  '( Рекурсивной = 0 | Итерационной = 1 | Для обеих = 2 ): '))
while o != 0 and o != 1 and o != 2:
    o = int(input('\nПринимаются только значения "0", "1" или "2": '))

# Вычисление времени + Графики
if (n >=  33 and (o == 0 or o == 2)) or (n >= 5000 and (o == 1 or o == 2)):
    k = int(input('\nЧисло n слишком большое. Работа программы может занять существенное время.'
                  ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
    while k != 0 and k != 1:
        k = int(input('\nПринимаются только значения "1" или "0": '))

if o == 0 and k == 1:
    for i in graf:
        start = time.time()
        res = F_rec(i)
        end = time.time()
        timer.append(end-start)
        rec_times = end - start
        print('№',i,"Результат рекурсии = ",res,"\nВремя выполнения = ",end-start,"\n\n")
    # Графики
    plt.plot(graf, timer, label='Рекурсионная функция.')
    plt.legend(loc=2)

if o == 1 and k == 1:
    for i in graf:
        start = time.time()
        result = F_iter(i)
        end = time.time()
        timer.append(end - start)
        iter_times = end - start
        print('№',i,"Результат итерации = ",result,"\nВремя выполнения = ",end-start,"\n\n")
    # Графики
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.legend(loc=2)

if o == 2 and k == 1:
    for i in graf:
        start = time.time()
        result = F_iter(i)
        end = time.time()
        timer.append(end-start)
        start_rec = time.time()
        res = F_rec(i)
        end_rec = time.time()
        timer_rec.append(end_rec-start_rec)
        rec_times = end_rec-start_rec
        iter_times = end-start
        print("\n",'№',i,"Результат рекурсии = ", res,"---------Результат итерации = ",result,"-----------Время  Рекурсии = ",end_rec-start_rec,"-------Время  Итерации = ",end-start)
    # Графики
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.plot(graf, timer_rec, label='Рекусионная функция.')
    plt.legend(loc=2)

if k == 0:
    print('\nРабота программы завершена.')
    quit()

plt.xlabel('Значение n')
plt.ylabel('Время выполнения (c)')
plt.show()

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from itertools import combinations
import random
import time

MAX_GROUP = 10

def run_program():
    try:
        N = int(entry_n.get())
        budget = int(entry_budget.get())
        # Считываем зарплаты: если пусто — генерируем, иначе парсим
        s_str = entry_salaries.get().strip()
        if s_str:
            salaries = [int(x) for x in s_str.split()]
            if len(salaries) != N:
                raise ValueError("Длина списка зарплат не совпадает с числом людей.")
        else:
            salaries = [random.randint(50, 200) for _ in range(N)]

        # Вывод зарплат
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"Зарплаты: {salaries}\n\n")

        # -------- Ограничение --------
        def check_group(group):
            total_salary = sum(salaries[i] for i in group)
            return total_salary <= budget

        # -------- Целевая функция --------
        def group_value(group):
            return sum(salaries[i] for i in group)

        # ----- Алгоритмический -----
        t1 = time.time()
        best_group, best_value = None, 0

        for size in range(1, min(MAX_GROUP, N)+1):
            subgroup = list(range(size))
            while True:
                if check_group(subgroup):
                    val = group_value(subgroup)
                    if val > best_value:
                        best_value = val
                        best_group = subgroup.copy()
                # движение по комбинаторике
                for i in reversed(range(size)):
                    if subgroup[i] != N - size + i:
                        break
                else:
                    break
                subgroup[i] += 1
                for j in range(i+1, size):
                    subgroup[j] = subgroup[j-1] + 1
        t2 = time.time()

        if best_group:
            text_result.insert(tk.END, f"АЛГОРИТМИЧЕСКИЙ ПОДХОД\n")
            text_result.insert(tk.END, f"Лучший состав: {[i+1 for i in best_group]}\n")
            text_result.insert(tk.END, f"Суммарная зарплата: {best_value}\n")
            text_result.insert(tk.END, f"Время: {t2-t1:.5f} сек.\n\n")
        else:
            text_result.insert(tk.END, "Нет подходящей подгруппы (алгоритмический).\n\n")

        # ----- Функциональный -----
        t1 = time.time()
        best_group_f, best_value_f = None, 0
        for size in range(1, min(MAX_GROUP,N)+1):
            for group in combinations(range(N), size):
                if check_group(group):
                    val = group_value(group)
                    if val > best_value_f:
                        best_value_f = val
                        best_group_f = group
        t2 = time.time()

        if best_group_f:
            text_result.insert(tk.END, f"ФУНКЦИОНАЛЬНЫЙ ПОДХОД\n")
            text_result.insert(tk.END, f"Лучший состав: {[i+1 for i in best_group_f]}\n")
            text_result.insert(tk.END, f"Суммарная зарплата: {best_value_f}\n")
            text_result.insert(tk.END, f"Время: {t2-t1:.5f} сек.\n")
        else:
            text_result.insert(tk.END, "Нет подходящей подгруппы (функциональный).\n\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Проверь ввод: {e}")

app = tk.Tk()
app.title("Оптимальные подгруппы")

frame_input = tk.Frame(app)
frame_input.pack(pady=10)
tk.Label(frame_input, text="Кол-во человек (N):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(frame_input, width=5)
entry_n.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Бюджет:").grid(row=0, column=2, padx=5, pady=5)
entry_budget = tk.Entry(frame_input, width=10)
entry_budget.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Зарплаты (через пробел, опционально):").grid(row=1, column=0, padx=5, pady=5, columnspan=2)
entry_salaries = tk.Entry(frame_input, width=40)
entry_salaries.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

frame_buttons = tk.Frame(app)
frame_buttons.pack(pady=5)
tk.Button(frame_buttons, text="НАЙТИ оптимум", command=run_program).grid(row=0, column=0, padx=5, pady=5)

frame_result = tk.Frame(app)
frame_result.pack(pady=10)
tk.Label(frame_result, text="Результаты:").pack()
text_result = scrolledtext.ScrolledText(frame_result, width=70, height=18)
text_result.pack()

app.mainloop()

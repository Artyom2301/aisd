'''17. Объекты – товар в магазине
Функции:	сегментация полного списка товара по категориям
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка товара по продажам
визуализация предыдущей функции в форме круговой диаграммы
'''

import csv
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from collections import defaultdict

# Класс для представления товара
class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        if price:
            self.price = float(price)
        else:
            self.price = None
        if quantity:
            self.quantity = int(quantity)
        else:
            self.quantity = None

    # Метод для вывода информации о товаре
    def __str__(self):
        return f'{self.name}: Категория - {self.category}, Цена - {self.price}'

# Функция для чтения данных из CSV файла
def read_csv_file():
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                product = Product(row['Name'], row['Category'], row.get('Price'), row.get('Quantity'))
                products.append(product)
            return products
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

# Функция для сегментации товаров по категориям
def segment_by_categories(products):
    categories = defaultdict(list)
    for product in products:
        categories[product.category].append(product)
    return categories

# Функция для сегментации товаров по продажам
def segment_by_sales(products):
    sales = defaultdict(list)
    for product in products:
        if product.price is not None:
            total_sales = product.price * product.quantity
            sales[total_sales].append(product)
    return sales

# Функция для выполнения сегментации по продажам и последующей визуализации
def perform_segmentation_by_sales():
    global sales
    sales = segment_by_sales(products)
    visualize_segmentation_by_sales(sales)

# Функция для выполняемой сегментации по категориям и последующей визуализации
def perform_segmentation_by_categories():
    global categories
    categories = segment_by_categories(products)
    visualize_segmentation_by_categories(categories)

# Функция для визуализации распределения товаров по категориям
def visualize_segmentation_by_categories(categories):
    labels = list(categories.keys())
    sizes = [len(categories[label]) for label in labels]
    explode = [0.1] * len(labels)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Для получения равномерной диаграммы
    plt.title("Сегментация товаров по категориям")
    plt.show()

# Функция для визуализации распределения товаров по продажам
def visualize_segmentation_by_sales(sales):
    values = list(sales.keys())
    counts = [len(sales[value]) for value in values]
    explode = [0.1] * len(values)
    fig2, ax2 = plt.subplots()
    ax2.pie(counts, explode=explode, labels=[f"{value:.2f}" for value in values], autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Для получения равномерной диаграммы
    plt.title("Сегментация товаров по продажам")
    plt.show()

# Создаем графический интерфейс с помощью библиотеки tkinter
root = tk.Tk()
root.title("Анализ товаров")

# Окно с информацией о товарах
info_frame = tk.Frame(root)
info_frame.pack(padx=10, pady=10)
tk.Label(info_frame, text="Информация о товарах").pack()

# Кнопка для загрузки данных из CSV файла
load_button = tk.Button(info_frame, text="Загрузить данные", command=lambda: load_data())
load_button.pack(pady=(10, 0))

# Метка для отображения статуса загрузки данных
info_label = tk.Label(info_frame, text="Нажмите кнопку для загрузки данных.")
info_label.pack(pady=(10, 0))

# Виджет для отображения результатов сегментации по категориям
segment_categories_frame = tk.Frame(root)
segment_categories_frame.pack(padx=10, pady=10)
tk.Label(segment_categories_frame, text="Сегментация по категориям").pack()

# Кнопка для запуска сегментации по категориям
segment_categories_button = tk.Button(segment_categories_frame, text="Выполнить сегментацию", command=lambda: perform_segmentation_by_categories())
segment_categories_button.pack(pady=(10, 0))

# Виджет для отображения результатов сегментации по продажам
segment_sales_frame = tk.Frame(root)
segment_sales_frame.pack(padx=10, pady=10)
tk.Label(segment_sales_frame, text="Сегментация по продажам").pack()

# Кнопка для запуска сегментации по продажам
segment_sales_button = tk.Button(segment_sales_frame, text="Выполнить сегментацию", command=lambda: perform_segmentation_by_sales())
segment_sales_button.pack(pady=(10, 0))

# Глобальные переменные для хранения продуктов и результатов сегментации
products = []
categories = {}
sales = {}

# Функция для загрузки данных
def load_data():
    global products
    products = read_csv_file()
    if products:
        info_label.config(text=f"Успешная загрузка данных: {len(products)} товаров.")
    else:
        info_label.config(text="Ошибка при загрузке данных.")

# Запуск главного цикла приложения
root.mainloop()

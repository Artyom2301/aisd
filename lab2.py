import re

# Функция проверяет, является ли строка числом (все символы — цифры)
def is_number(lexeme):
    return lexeme.isdigit()

# Функция преобразует число в слова по цифрам
def number_to_words(number):
    digits_map = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digits_map[d] for d in str(number))

# Функция обрабатывает одну возрастающую последовательность
def process_sequence(seq):
    if len(seq) >= 2:  # Учитываем только последовательности длиной от 2 чисел
        min_val = min(seq)
        print(f"Минимальное число в последовательности: {min_val}")
        print(f"Прописью: {number_to_words(min_val)}\n")

# === Основная часть программы ===

# Читаем весь файл сразу
with open('test1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Используем регулярное выражение для поиска всех "лексем":
# \d+ — числа, \D+ — нечисловые блоки
lexemes = re.findall(r'\d+|\D+', text)

# Инициализируем переменные для отслеживания последовательностей
current_sequence = []
previous_number = None

# Перебираем все лексемы
for lex in lexemes:
    lex = lex.strip()  # Убираем пробелы и переносы строк по краям

    if not lex:
        continue  # Пропускаем пустые строки

    if is_number(lex):
        number = int(lex)

        if previous_number is None or number > previous_number:
            current_sequence.append(number)
            previous_number = number
        else:
            process_sequence(current_sequence)
            current_sequence = [number]
            previous_number = number
    else:
        # Если лексема не число — последовательность обрывается
        if current_sequence:
            process_sequence(current_sequence)
            current_sequence = []
            previous_number = None

# После завершения цикла — проверяем, не осталась ли необработанная последовательность
if current_sequence:
    process_sequence(current_sequence)

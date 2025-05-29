def is_number(lexeme):
    return lexeme.isdigit()

def number_to_words(number):
    digits_map = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digits_map[d] for d in str(number))

def process_sequence(seq):
    if len(seq) >= 2:
        min_val = min(seq)
        print(f"Минимальное число в последовательности: {min_val}")
        print(f"Прописью: {number_to_words(min_val)}\n")

# Настройки
buffer_len = 1
max_buffer_len = 100
razd = [' ']

current_lexeme = ''
current_sequence = []
previous_number = None

with open('test1.txt', 'r', encoding='utf-8') as file:
    buffer = file.read(buffer_len)
    if not buffer:
        print("Файл пуст.")
    while buffer:
        if buffer in razd:
            if is_number(current_lexeme):
                number = int(current_lexeme)
                if previous_number is None or number > previous_number:
                    current_sequence.append(number)
                    previous_number = number
                else:
                    process_sequence(current_sequence)
                    current_sequence = [number]
                    previous_number = number
            else:
                # Если встретили не число, завершаем текущую последовательность
                if current_sequence:
                    process_sequence(current_sequence)
                    current_sequence = []
                    previous_number = None
            current_lexeme = ''
        else:
            current_lexeme += buffer
        buffer = file.read(buffer_len)

# Последняя лексема
if is_number(current_lexeme):
    number = int(current_lexeme)
    if previous_number is None or number > previous_number:
        current_sequence.append(number)
    else:
        process_sequence(current_sequence)
        current_sequence = [number]

# Последняя последовательность
if current_sequence:
    process_sequence(current_sequence)

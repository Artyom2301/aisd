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

current_sequence = []
previous_number = None

with open('test1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lexemes = content.split(' ') 

    for lexeme in lexemes:
        if is_number(lexeme):
            number = int(lexeme)
            if previous_number is None or number > previous_number:
                current_sequence.append(number)
                previous_number = number
            else:
                process_sequence(current_sequence)
                current_sequence = [number]
                previous_number = number
        else:
            if current_sequence:
                process_sequence(current_sequence)
                current_sequence = []
                previous_number = None

if current_sequence:
    process_sequence(current_sequence)

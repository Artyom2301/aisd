import re

def number_to_words(n):
    d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
         '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
    return ' '.join(d[i] for i in str(n))

def process(s):
    if len(s) > 1:
        m = min(s)
        print(f"Минимальное число в последовательности: {m}\nПрописью: {number_to_words(m)}\n")

with open('test1.txt', encoding='utf-8') as f:
    nums = list(map(int, re.findall(r'\d+', f.read())))

seq, prev = [], None
for n in nums:
    if prev is None or n > prev:
        seq.append(n)
        prev = n
    else:
        process(seq)
        seq, prev = [n], n
if seq: process(seq)

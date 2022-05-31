import sys
import pymorphy2
from string import punctuation

morph, text = pymorphy2.MorphAnalyzer(), sys.stdin.read().lower() 
words = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
for i in punctuation:
    text = text.replace(i, ' ')
answer = 0
for i in text.split():
    if morph.parse(i)[0].normal_form in words:
        answer += 1
print(answer)
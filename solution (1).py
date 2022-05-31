import pymorphy2
import sys


morph = pymorphy2.MorphAnalyzer()
text = sys.stdin.read().lower()
text = ''.join([i if i in 'ёйцукенгшщзхъыфывапролджэячсмитьбю ' else ' ' for i in text])
words = []
for i in text.split():
    temp = morph.parse(i)
    if 'NOUN' in temp[0].tag and temp[0].score > 0.5:
        words.append(temp[0].normal_form)
words = sorted(set([(i, words.count(i)) for i in words]), key=lambda x: (x[1], x[0]), reverse=True)
words = [i[0] for i in words][:10]
print(' '.join(words))
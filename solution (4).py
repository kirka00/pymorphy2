import pymorphy2
import sys


morph = pymorphy2.MorphAnalyzer()
text = sys.stdin.read().lower()
text = ''.join([i if i in 'ёйцукенгшщзхъыфывапролджэячсмитьбю' else ' ' for i in text]).split()

for i in text:
    word = morph.parse(i)[0]
    
    if 'NOUN' in word.tag:
        if word.tag.animacy == 'anim':
            if word.tag.number == 'plur':
                print('Живые')
            else:
                if word.tag.gender == 'masc':
                    print('Живой')
                elif word.tag.gender == 'femn':
                    print('Живая')
                else:
                    print('Живое')
        else:
            if word.tag.number == 'plur':
                print('Не живые')
            else:
                if word.tag.gender == 'masc':
                    print('Не живой')
                elif word.tag.gender == 'femn':
                    print('Не живая')
                else:
                    print('Не живое')
    else:
        print('Не существительное')
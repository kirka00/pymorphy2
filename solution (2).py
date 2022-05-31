import pymorphy2


morph = pymorphy2.MorphAnalyzer()
word = morph.parse(input().lower())[0]

a = [('sing', 'Единственное'), ('plur', 'Множественное')]

b = [('nomn', 'Именительный'),
     ('gent', 'Родительный'),
     ('datv', 'Дательный'),
     ('accs', 'Винительный'),
     ('ablt', 'Творительный'),
     ('loct', 'Предложный')]

if 'NOUN' in word.tag:
    for i in a:
        print(f'{i[1]} число:')
        for j in b:
            print(f'{j[1]} падеж: {word.inflect({i[0], j[0]}).word}')
else:
    print('Не существительное')
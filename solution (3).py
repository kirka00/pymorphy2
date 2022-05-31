import pymorphy2
morph = pymorphy2.MorphAnalyzer()

word = input().lower()
word = morph.parse(word)[0]

a = ['past', 'Прошедшее время:']
b = ['masc', 'femn', 'neut', 'plur']
c = ['pres', 'Настоящее время:']
d = [('1per', 'sing'),
     ('1per', 'plur'),
     ('2per', 'sing'),
     ('2per', 'plur'),
     ('3per', 'sing'),
     ('3per', 'plur')]


if word.tag.POS in {'INFN', 'VERB'}:
    print(a[1])
    for i in b:
        print(word.inflect({a[0], i}).word)
    print(c[1])
    for j in d:
        print(word.inflect({c[0], j[0], j[1]}).word)
else:
    print('Не глагол')
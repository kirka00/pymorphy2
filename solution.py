import pymorphy2


morph = pymorphy2.MorphAnalyzer()
word = morph.parse('бутылка')[0]


for i in range(99, 0, -1):
    print(f'В холодильнике {i} {word.make_agree_with_number(i).word} кваса.\n'
          f'Возьмём одну и выпьем.')
    i -= 1
    if i != 11 and i % 10 == 1:
        print(f'Осталась {i} {word.make_agree_with_number(i).word} кваса.')
    else:
        print(f'Осталось {i} {word.make_agree_with_number(i).word} кваса.')
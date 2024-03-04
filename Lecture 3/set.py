colors = set()
colors = {'red', 'green', 'blue'} #содержит только уникальные значения
print(colors)

colors.add('red')
print(colors)

colors.add('grey')
print(colors)

colors.remove('red') # если red нет в множестве при поаытке удаления выведется ошибка
print(colors)

colors.discard('red') # если red нет в множестве при поаытке удаления не выведется ошибка
print(colors)

colors.clear()
print(colors)
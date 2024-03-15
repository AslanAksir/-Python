list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))# для функции map в скобках даны аргументы : функция lambda x: x + 10 
# и объект list_1 к которому эта функция применяется
print(list_1)
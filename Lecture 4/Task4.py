# Выбрать из списка четные числа и составить список пар (число; квадрат числа)
# Пример: 1 2 3 5 8 15 23 38  Вывод: [(2, 4), (8, 64), (38, 1444)]

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []
# for i in list1:
#     if i % 2 == 0:
#         res.append((i, i*i))

# print(res)


def select(f, col):
    return [f(x) for x in col] # возвращает список в котором к каждому элементу применена функция f(x)

def where(f, col):
    return [x for x in col if f(x)] # возвращает список значений, которые соотвествуют условию f(x)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x%2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)
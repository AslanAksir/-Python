# data = [15, 65, 9, 36,175]
# res = list(filter(lambda x: x % 10 == 5, data))# выводит (отфильтровывает) только числа, которые делятся на 5
# print(res)

# похожа на функцю where из задачи 4

# def where(f, col):
#     return [x for x in col if f(x)] # возвращает список значений, которые соотвествуют условию f(x)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data) # вместо select подставили map
print(res)
# res = where(lambda x: x%2 == 0, res)
res = filter(lambda x: x%2 == 0, res) # вместо where подставили filter
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)
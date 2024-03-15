# перевести строку из чисел в список из чисел
data = '15 156 96 3 5 8 52 5'
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)

# функция select(int, data) из задачи 4 по существу совпадает с map
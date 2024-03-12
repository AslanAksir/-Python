# Определить в массиве целых чисел количество элементов для которых два соседних элемента меньше этих элементов.
# ввод 5
# 1 2 3 4 5
# вывод 0

# ввод 1 5 1 5 1
# вывод 2

n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

count = 0
for i in range(1, n-1):
    # if list1[i - 1] < list1[i] and list1[i] > list1[i + 1]:
    if list1[i - 1] < list1[i] > list1[i + 1]:
        count += 1

print(count)


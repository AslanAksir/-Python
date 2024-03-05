# Подсчитать количество элементов массива, больших предыдущего (элемента с предыдущим номером)

list1 = [0, -1, 5, 2, 3]
result = 0
for i in range(len(list1) - 1):
    if list1[i] < list1[i+1]:
        result += 1
print(result)
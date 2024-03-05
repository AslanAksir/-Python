# Циклически сдвинуть последовательность N вправо на K элементов. K > 0
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# for i in range(0, k):
#     list_1.append(list_1[0])
#     list_1.pop(0)
#     print(list_1)

list1 = [5, 4, 6, 7, -10]
k = int(input())
k = k % len(list1)

list_res = []
for i in range(k):
    list_res.append(list1[len(list1) - 1 - i])
for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list1)
print(list_res)

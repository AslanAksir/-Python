# вывести последовательность из N элементов в обратном порядке
# использовать циклы и объявлять массивы нельзя

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n-1) + f'{k}'

n = int(input())
print(f(n))

# Найти n-е число Фибоначчи


def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n - 1) + f(n - 2)

n = int(input())
print(f(n - 2))

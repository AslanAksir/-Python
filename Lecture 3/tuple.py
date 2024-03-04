t = ()
print(type(t))  # число tuple

t = (1)
print(type(t)) # число int

t = (1,) # tuple требует поставить запятую
print(type(t))  # число tuple

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b = 1, 2 # множественное присваивание
a = b = 1

t = (1, 2, 3, 5)
for i in t:
    print(t[i-2])

t[1] = 0 # выдаст ошибку т.к. кортеж нельзя изменить

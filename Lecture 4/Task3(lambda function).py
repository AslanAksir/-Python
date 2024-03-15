# def calk1(a, b):
#     return a+b

def calk2(a, b):
    return a*b

def math(op, x, y): # в op бует передаваться функция с аргументом x, y
    print(op(x, y))

# calk1 = lambda a, b: a + b

# math(calk1, 5, 45)
# math(calk2, 5)

math(lambda a, b: a + b, 5, 45)
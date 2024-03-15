def calk1(a):
    return a+a

def calk2(a):
    return a*a

def math(op, x): # в op бует передаваться функция с аргументом x
    print(op(x))

math(calk1, 5)
math(calk2, 5)
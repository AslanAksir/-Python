# функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных
#по минимальному входящему набору
users = ['users1', 'users2', 'users3', 'users4', 'users5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)


users = ['users1', 'users2', 'users3', 'users4', 'users5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)
d = {}
d = dict()

d['q'] = 'qwerty'
print(d) 

d['w'] = 'werty'
print(d) 

print(d['q'])

d[895] = 9898
print(d)

del d[895]
print(d)

for item in d:
    print(item)
    print('{}: {}'.format(item, d[item]))

print(d.items())
for (k, v) in d.items():
    print(k, v)
    
x = [1,2,3,4,5,6]
y = ['a','b','c','e','f','e']

z = []
for a in x:
    for b in y:
        z.append((a,b))
print(z)

z = [(a,b) for a in x for b in y]
print(z)
#使用多個for clause

x = [1,2,3,4,5]  
y = ['a','b','c','d','e'] 
z = [(a,b) for a in x for b in y]
print(z)

# 相當於
for a in x:
    for b in y:
        z.append((a,b))
print(z)
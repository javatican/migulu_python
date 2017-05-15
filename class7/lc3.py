x= [1,2,3,4,5,6,7,8,9,10]
y=[4,6,9]

z=[]
for a in x:
    if a not in y:
        z.append(a)
print(z)

# list comprehension

z = [a for a in x if a not in y]
print(z)
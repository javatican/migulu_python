x = [1,2,3,4,5,6]
#y=[11,12,13,14,15,16]
y = []
for a in x:
    y.append(a+10)
print(y)

# list comprehension語法

y = [a+10 for a in x]
print(y)

y=[a+10 for a in x if a%2]
print(y)
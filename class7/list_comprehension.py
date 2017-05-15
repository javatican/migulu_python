x = [1,2,3,4,5] #欲產生一個[11,12,13,14,15]

#1
y = []
for a in x:
    y.append(a+10);
print(y)

#2
y = [a+10 for a in x]
print(y)

# 使用filter
z = [a for a in x if a%2]
print(z)
#print Fibonacci series

n=0
m=1
for x in range(1,11):
    target=n+m
    print(target)
    n=m
    m=target
    
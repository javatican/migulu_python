n=0
m=1
for x in range(1,20):
    new_m=n+m
    print(new_m,", golden ratio:" ,n/m)
    n=m
    m=new_m
    
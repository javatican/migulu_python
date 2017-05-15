x=-101
if x%2 and x>0:
    print(x,"是正奇數")
elif x%2 and x<0:
    print(x,"是負奇數")
elif x%2==0 and x>0:
    print(x,"是正偶數")
elif x%2==0 and x<0:
    print(x,"是負偶數")
else:
    print(x,"是0")
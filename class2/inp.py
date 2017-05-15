while True:
    x = input("請輸入一個字元: "); 
    if len(x)==1 :
        if ord(x)>=65 and ord(x)<=90:
            print(x,"是大寫字母")
        elif ord(x)>=97 and ord(x)<=122:
            print(x,"是小寫字母")
        elif ord(x)>=48 and ord(x)<=57:
            print(x,"是一個阿拉伯數字")
        else:
            print(x,"不是英文字母, 或數字")
        
        break;
    else:
        print("您輸入的資料超過一個字元")
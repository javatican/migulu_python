while True:
    x = input("請輸入一個字元: "); 
    if len(x)==1 :
        if x>='A' and  x<='Z':
            print(x,"是大寫字母")
        elif ord(x) in range(ord('a'),ord('z')):
            print(x,"是小寫字母")
        elif x>='0' and x<='9':
            print(x,"是一個阿拉伯數字")
        else:
            print(x,"不是英文字母, 或數字")
        
        break;
    else:
        print("您輸入的資料超過一個字元") 
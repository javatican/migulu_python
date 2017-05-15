def is_upper(x):
    if x>='A' and  x<='Z':
        return True
    else:
        return False
def is_lower(x):
    if x>='a' and  x<='z':
        return True
    else:
        return False

def is_digit(x):
    if x>='0' and  x<='9':
        return True
    else:
        return False

while True:
    x = input("請輸入一個字元: "); 
    if len(x)==1 :
        if is_upper(x):
            print(x,"是大寫字母")
        elif is_lower(x):
            print(x,"是小寫字母")
        elif is_digit(x):
            print(x,"是一個阿拉伯數字")
        else:
            print(x,"不是英文字母, 或數字")
        
        break;
    else:
        print("您輸入的資料超過一個字元") 
def is_upper(input='A'):
    """check if input is an upper case character """
    if input>='A' and input <='Z':
        return True
    else:
        return False
        
def is_lower(input):
    if  x>='a' and x<='z':
        return True
    else:
        return False
        
def is_digit(input):
    if x>='0' and x<='9':
        return True
    else:
        return False
        
while True:
    x = input("請輸入一個字元: ");
    if len(x)!=1:
        print("您輸入的不是單一字元!")
        continue
    else:
        break
    
if is_upper(x):
    print(x,"是大寫字母")
elif is_lower(x):
    print(x,"是小寫字母")
elif is_digit(x):
    print(x,"是阿拉伯數字")
else:
    print(x,"不是英文字母或數字")


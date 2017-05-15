def func1(a):
    print("id(a)=",id(a),",a=",a)
    a+=1
    print("id(a)=",id(a),",a=",a)

x=100
print("id(x)=",id(x),",x=",x)
func1(x)
print("id(x)=",id(x),",a=",x)


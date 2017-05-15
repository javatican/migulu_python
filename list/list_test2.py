s1 = [1,2,3,4,5,3]
s2 = ['John','Mary','Tom','Eddie','Helen']
# x in s
print(1 in s1)
print('Tom' in s2)
# x not in s
print('Sam' not in s1)
# use + 
print(s1+s2)  
#s*n or n*s
print(s1*3)
print(3*s2)
# s[i] , 若i為負值, 相當於len(s)+ i
print(s1[1])
print(s1[-1]) #相當於s1[5]
# s[i:j]
print(s1[1:3])
print(s1[:3])
print(s1[1:])
# s[i:j:k]
print(s1[1:4:2])
# len(s)
print(len(s2))
# min(s)
print(min(s1))
# max(s)
print(max(s2))
# s.index(x)
print(s1.index(3))
#print(s2.index('Scot')) # raise ValueError
print(s1.index(3,2,5))
# s.count(x)
print(s1.count(3))

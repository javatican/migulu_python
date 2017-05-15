import io
s1 = "abcdefg"
s2 = "hijklmn"
# x in s
print('a' in s1)
print('ab' in s1)
# x not in s
print('x' not in s1)
# use + 
print(s1+s2)
# use str.join()
print("\t".join([s1,s2]))
# use in-memory stream
output = io.StringIO()
output.write(s1)
print(s2,file=output)
print(output.getvalue())
output.close()
#s*n or n*s
print(s1*3)
print(3*s2)
# s[i] , 若i為負值, 相當於len(s)+ i
print(s1[1])
print(s1[-1]) #相當於s1[6]
# s[i:j]
print(s1[1:3])
print(s1[:3])
print(s1[1:])
# s[i:j:k]
print(s1[1:6:2])
# len(s)
print(len(s2))
# min(s)
print(min(s1))
# max(s)
print(max(s1))
# s.index(x)
print(s1.index('b'))
print(s2.index('a')) # raise ValueError
print(s1.index('b',3,6))
# s.count(x)
print(s2.count('a'))

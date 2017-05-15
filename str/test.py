import io


# in
s1="abcdefg"
print('a' in s1)
print('ab' in s1)
print('x' in s1)
# not in
print('x' not in s1)
s2="0101"
print(s1+s2)
print("".join([s1,s2]))
# in-memory stream
output = io.StringIO()
output.write(s1)
output.write(s2)
print(output.getvalue())
output.close()
# s1*3
print(s1*3)
print(3*s2)
# index
print(s1[5])
print(s1[1:4])
print(s1[1:5:2])
print(s1[:4])
print(s1[1:])
#
print(s1[-1])
#
print(len(s1))
print(max(s1))
print(min(s1))
#index()
print(s1.index('e'))
if 'x' in s1:
    print(s1.index('x'))
#count()
print(s1.count('ab'))

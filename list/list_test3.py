s1 = [1,2,3,4,5,3]
s2 = ['Ed','Mary','Tom','Christopher','Helen']
# s[i] = x
s1[3]=10
print(s1)
#s[i:j] = t
s1[2:4] = [20]
print(s1)
s1[2:4] = [11,12,13,14]
print(s1)
#del s[i:j]
del s2[1:3]
print(s2)
#s[i:j:k] = t
#t must have the same length as the slice it is replacing.
s1[1:6:2] = [25,26,27]
print(s1)
#del s[i:j:k]
del s1[1:6:2] 
print(s1)
#s.append(x)
s2.append("May")
s2.append("Vincent")
print(s2)
#s.copy()
s3= s1.copy()
print(s3)
#s.clear()
s1.clear()
print(s1)
#s.extend(t) or s += t
s1.extend(s3)
print(s1)
s2.extend(['Henry','Peter'])
print(s2)
s1+=[5,6,7]
print(s1)
#s *= n
s1*=2
print(s1)
#s.insert(i, x)
s2.insert(-3,'Ryan')
print(s2)
#s.pop([i])
# i default to -1, so the last item is removed and returned
print(s2.pop())
print(s2)
#s.remove(x)
# raise ValueError if x is not found
#s2.remove('Candy') 
s2.remove('Ryan')
print(s2)
#s.reverse()
s2.reverse()
print(s2)
#sort(*, key=None, reverse=None)
s2.sort()
print(s2) 
s2.sort(reverse=True)
print(s2) 
s2.sort(key=len)
print(s2) 
import io
s1 = "abcdefg中文cde"
s2 = "hijklmn"
# str.encode(encoding="utf-8", errors="strict")
print(s1.encode())
# str.find(sub[, start[, end]]), str.rfind(sub[, start[, end]])
print(s1.find('c'))
print(s1.find('c',3,5))
print(s1.find('x')) # return -1 if not found
print(s1.rfind('c'))
# str.format(*args, **kwargs)
print("1+2={0},2*3={1}".format(1+2,2*3))
print("My firstname={first},lastname={last}".format(last="Nieh",first="Ryan"))
# str.strip([chars]), str.lstrip([chars]),  str.rstrip([chars])
s3 = "    abc   "
print("'{0}'".format(s3.strip()))
print("'{0}'".format(s3.lstrip()))
print("'{0}'".format(s3.rstrip()))
# str.partition(sep), str.rpartition(sep)
s4="ryan@yahoo.com.tw"
print(s4.partition('@')) 
print(s4.partition('.')) 
print(s4.rpartition('.')) 
# str.replace(old, new[, count])
s5="tw000tw111tw222tw333"
print(s5.replace('tw','TW',2))
# str.split(sep=None, maxsplit=-1), str.rsplit(sep=None, maxsplit=-1)
s6='12.34.56.78.90'
s7='.12.34.56..78.90.'
print(s6.split('.'))
print(s7.split('.'))
print(s6.split('.',maxsplit=2))
s8='a b c d e'
s9=' a  b  c  d  e '
print(s8.split())
print(s9.split())
# str.splitlines([keepends])
s10="""this is 1st line
this is 2nd line
this is 3rd line
this is 4th line """
print(s10.splitlines())
print(s10.splitlines(True))
# str.startswith(prefix[, start[, end]])
# str.endswith(prefix[, start[, end]])
s11="migulu001.py"
print(s11.startswith('migulu'))
print(s11.endswith('.py'))
# str.join(iterable)
l1 = s6.split('.')
print(l1)
print(",".join(l1))
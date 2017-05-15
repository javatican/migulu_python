s1="fsfs中文fsfs"
print(s1.encode("utf-8"))
print(s1.rfind("fs"))
print(s1.find("x"))
#format
print("1+2={0}, 2*3={1}".format(1+2, 2*3))
print("Good {0}, {1}!".format("morning","Ryan"))
print("{1}, Good {0}!".format("morning","Ryan"))
#
print("Good {time}, {name}!".format(time="morning", name="Ryan"))
print("Good {time}, {name}!".format(name="Ryan", time="morning"))
# strip(), rstrip(), lstrip()
s2="   abc    "
print(s2.strip())
#partition()
s3="ryan.nieh@gmail.com"
print(s3.partition('@')) # 3-element tuple
#
s4='123.234.567'
print(s4.partition('.'))
print(s4.rpartition('.'))
#replace()
print(s1.replace('fs',"ps"))
print(s1.replace('fs',"ps",2))
print(s1)
#s1=s1.replace('fs','ps')
print(s1)
#split()
print(s4.split('.',1))
print(s3.split('@'))
s5="123.456..789"
print(s5.split('.'))
#splitlines()
s6="""fsfs;fsfsfslfls
jfslkfjsl
jffffffff
"""
print(s6.splitlines())
#startswith()
#endswith()
print(s1.startswith('fs'))
print(s1.endswith('fs'))
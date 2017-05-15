print("1+2={0}".format(1+2))
print("1+2=%d" % 3) # %d decimal integer
print("Good {0}, {1}!".format('morning','Ryan'))
print("Good %s, %s!" % ('morning', 'Ryan')) #%s string, 參數必須使用tuple語法
print("1.2+3.5=%f" % 4.7)

print("My name is %(name)s, my age is %(age)d. My ID is %(id)s" % {'name':'Ryan','age':40, 'id':'007'})
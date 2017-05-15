#printf-style string formatting
print("Good %s!" % "Morning")
print("Welcome to my site, %s. You are no. %d visitor." % ('Ryan',39))
print("My name is %(name)s. I am %(age)d years old. My ID is %(id)03d." %
{'name':'Ryan', 'age':40, 'id':7})
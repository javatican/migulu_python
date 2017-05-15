class Foo(object):
    def __mangled_method(self):
        print("mangled method in Foo")
    def call_mangled(self):
        self.__mangled_method();
         
class SubClass(Foo):
    def __mangled_method(self):
        print("mangled method in SubClass")
        
print(dir(Foo))
print(dir(SubClass))

f = Foo() 
f.call_mangled()

f2=SubClass()
f2.call_mangled()

print(SubClass.__base__)
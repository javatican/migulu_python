class Y(object): 
    def c1(cls, *args): 
        print( 'c1', cls) 
    c1 = classmethod(c1)
    @classmethod 
    def c2(cls, *args): 
         print ('c2', cls)
y =Y()
y.c1()
y.c2()
Y.c1()
Y.c2()
 

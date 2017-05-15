
class Y(object): 
    def __init__(self, astring):
        self.s = astring
    @classmethod
    def fromlist(cls, alist): #factory method for creating object
        x = cls('')
        x.s = ','.join(str(s) for s in alist)
        return x
    def __repr__(self):
        return 'y(%r)' % self.s

y1 = Y('xx')
print(y1)
y2 = Y.fromlist(range(3))
print(y2)
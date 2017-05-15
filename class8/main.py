from Cat import Cat
from Dog import Dog
from Pet import Pet
c1 = Cat('xat1', 6)
c2 = Cat('gat2', 8)
d1 = Dog('aog1', 'black')
d2 = Dog('tog2','white')
l1 = list([c1,c2,d1,d2])
print(l1)
l1.reverse()
print(l1)
l1.sort(key=Pet.get_name, reverse=True)
print(l1)
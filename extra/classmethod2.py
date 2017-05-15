class Person:
    age = 25 # class variable

    def printAge(cls):
        print('The age is:', cls.age)
    @classmethod
    def printAge2(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()
Person.printAge2()
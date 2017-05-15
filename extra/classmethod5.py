from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
        
    @staticmethod
    def fromFatherAge(name, fatherBirthYear, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherBirthYear - fatherPersonAgeDiff)
        
    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex="Male"
     

man1 = Man.fromBirthYear('John',  1985)
man1.display()

man2 = Man.fromFatherAge('Tom', 1950, 30)
man2.display()

print(isinstance(man1,Man))
print(isinstance(man2,Man))

 

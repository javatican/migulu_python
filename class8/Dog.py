from Pet import Pet
from Pet import animal_speak
class Dog(Pet):
    def __init__(self, name, color):
        #self.name=name
        #self.species='Dog'
        #Pet.__init__(self,name,'Dog') # Python 2.0
        #super(Dog, self).__init__(name,'Dog') #Python 2.0
        super().__init__(name,'Dog') #python 3.0
        self.color = color
    def speak(self):
        print("旺旺!")
    def show(self):
        Pet.show(self)
        print("color=%s" % self.color)
    def __repr__(self):
        return "(name:%s,color:%s)" % (self.name, self.color)
def main():
    d1 = Dog("Money","black")
    animal_speak(d1)

if __name__ == "__main__":
    main()

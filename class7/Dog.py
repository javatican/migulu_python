from Pet import Pet
class Dog(Pet):
    def __init__(self, name, color):
        Pet.__init__(self,name,'Dog')
        #super(Dog, self).__init__(name,'Dog')
        #super().__init__(name,'Dog')
        self.color = color
    def speak(self):
        print("旺旺!")
    def show(self):
        Pet.show(self)
        print("color=%s" % self.color)

    def __str__(self):
        return "name=%s, species=%s, color=%s"  % (self.name, self.species, self.color)
def animal_speak(animal):
    animal.speak()
    
def main():
    d1 = Dog("Money","black")
     
    p1 = Pet("Candy","Fish")
    animal_speak(d1)
    animal_speak(p1)

if __name__ == "__main__":
    main()

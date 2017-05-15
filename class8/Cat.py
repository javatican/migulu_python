from Pet import Pet
from Pet import animal_speak
class Cat(Pet):
    def __init__(self, name, weight):
        super().__init__(name, 'Cat')
        self.weight = weight
    def speak(self):
        print("喵喵")
    def show(self):
        Pet.show(self)
        print("weight=%f" % self.weight)
    def __str__(self):
        return "[name=%s, weight=%f]" % (self.name, self.weight)
    def __repr__(self):
        return "(name:%s,weight:%f)" % (self.name, self.weight)
def main():
    c1 = Cat('Gartfield',10)
    c1.speak()
    c1.show()
    animal_speak(c1)
    print(c1)
    
if __name__=='__main__':
    main()
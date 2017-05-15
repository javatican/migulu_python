class Pet(object):
    def __init__(self, name, species): #建構子
        self.name = name;
        self.species = species;
    def speak(self):
        print("I am not sure if I can speak")
    def show(self):
        print("name=%s, species=%s" % (self.name, self.species))
    def get_name(self):
        return self.name

def animal_speak(animal):
    animal.speak()

        
def main():
    p1 = Pet("Money","Dog")
    animal_speak(p1)
    

if __name__ =="__main__":
    main()
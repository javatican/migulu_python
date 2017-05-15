class Pet(object):
    def __init__(self, name, species): #建構子
        self.name = name;
        self.species = species;
    def speak(self):
        print("I am not sure if I can speak")
    def show(self):
        print("name=%s, species=%s" % (self.name, self.species))
        
    def __str__(self):
        return "name=%s, species=%s" % (self.name, self.species)
        
    def __repr__(self):
        return "name=%s, species=%s" % (self.name, self.species)
def main():
    p1 = Pet("Money","Dog")
    p1.show()
    p2 = Pet("Garfield","Cat")
    p2.show()
    print(p1)

if __name__ =="__main__":
    main()
class Animal:
    def __init__(self,fur):
        self.fur = fur
        print("Animal Created!")
    def report(self):
        print("Animal")
    def eat(self):
        print("Eating!")
animal = Animal("Fuzzy")
animal.report()
animal.eat()

class Dog(Animal):
    def __init__(self,fur):
        print("Dog created")
dog = Dog("Fuzzy")
dog.report()
dog.eat()

class Cat(Animal):
    def __init__(self,fur):
        Animal.__init__(self,fur)
        print("Cat created")
        print(self.fur)
cat = Cat("jazzy")
cat.report()
cat.eat()

class Goat(Animal):
    def __init__(self,fur):
        Animal.__init__(self,fur)
        print("Goat created!")
        print(self.fur)
    def report(self):
        print("I am a goat!")
goat = Goat("no fur")
goat.report()
goat.eat()

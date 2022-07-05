class Dog:
    #Class object attributes
    species = "Mammal"
    def __init__(self,input_breed,input_name):
        self.breed = input_breed
        self.name = input_name

x = Dog( 'Huskie',"Sammy")
print(type(x))
print(x.breed)
print(x.name)
print(x.species)

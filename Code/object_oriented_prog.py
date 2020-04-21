#Object oriented programming (OOP)
#Allows creation of own objects that have
#methods and attributes

class Dog():
    #instance of the Dog() class
    def __init__(self,breed,name,spots): #breed is parameter name
        #Attributes 
        #We take the argument (breed)
        #Assign it using self.attibute_name (breed)
        self.breed = breed
        self.name = name
        #Expect bool T/F
        self.spots = spots

my_dog = Dog(breed='Lab',name='Homer',spots=False)

type(my_dog)

my_dog.breed
my_dog.name
my_dog.spots



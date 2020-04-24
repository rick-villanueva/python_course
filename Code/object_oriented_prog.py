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

#Class object attributes

class Dog():
    #CLASS OBJECT ATTRIBUTE, SAME OF ANY INSTANCE OF CLASS
    species = 'mammal' #regardles of instance
    #instance of the Dog() class
    def __init__(self,breed,name,spots): #breed is parameter name
        #Attributes 
        #We take the argument (breed)
        #Assign it using self.attibute_name (breed)
        self.breed = breed
        self.name = name
        #Expect bool T/F
        self.spots = spots
    
    #Operations/Actions done with classes --> Methods      
    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number)) #have to ref the 
        #particular instance of the name

my_dog = Dog(breed='Cocker',name='Homer',spots=False)

type(my_dog)

my_dog.breed
my_dog.name
my_dog.spots
my_dog.species  
my_dog.bark(10) #Method called differently

class Circle():
    #Class object attribute: Always true
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius*radius*Circle.pi
    
    #Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30) #changes the default val of radius

my_circle.pi
my_circle.radius 
my_circle.area
my_circle.get_circumference()

#Inheritance
class Animal():
    
    def __init__(self):
        print('Animal Created')
        
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')
        
myanimal = Animal()

myanimal.eat()

class Dog(Animal): #see the inheritance
    #CLASS OBJECT ATTRIBUTE, SAME OF ANY INSTANCE OF CLASS
    species = 'mammal' #regardles of instance
    #instance of the Dog() class
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
        
    def who_am_i(self): #override instances
        print('I am a dog')
        
    def bark(self):
        print('WOOF!')
        
my_dog = Dog()

my_dog.eat() #Reuse methods from previous class
my_dog.who_am_i()
my_dog.bark()

#Polymorphism 
class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says woof!'
    
class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says meow!'
    
niko = Dog('niko')
felix = Cat('felix')

niko.speak()
felix.speak()


for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(felix)

#base class
class Animal():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

#Classes where the method is used
class Dog(Animal):
    
    def speak(self):
        return self.name + ' says woof!'
    
class Cat(Animal):
    
    def speak(self):
        return self.name + ' says meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

fido.speak()
isis.speak()

#Special methods
class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    
    #special func to print   
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    #special func for len
    def __len__(self):
        return self.pages
    
    #special func for delete
    def __del__(self):
        print('A book object has been deleted')
        
b = Book('Inferno','Dante',500)

print(b)
len(b)

a = Book('Paradiso','Dante',800)

del a #deletes from memory

#Distance and slope
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1 #tuple unpackimg
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()

#Cylinder formulas
class Cylinder:
    
    pi = 3.1415

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (Cylinder.pi*(self.radius**2)*self.height)
    
    def surface_area(self):
        return ((2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*(self.radius**2)))

cylinder = Cylinder(2,3)

cylinder.volume()
cylinder.surface_area()

#Bank Account 
class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account owner: {} \nAccount balance: ${}'.format(self.owner,self.balance)

    def deposit(self,dp_amt):
        self.balance += dp_amt
        print('${} added to your account'.format(dp_amt))
        print('New account balance = ${}'.format(self.balance))

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('${} withdrawn from your account'.format(wd_amt))
            print('New account balance = ${}'.format(self.balance))
        else:
            print('Funds Unavailable!')
            
acct1 = Account('Rick',500)

print(acct1)

acct1.owner
acct1.balance
acct1.deposit(500)
acct1.withdraw(600)
acct1.withdraw(1200)
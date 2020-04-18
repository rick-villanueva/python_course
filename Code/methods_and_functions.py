#Functions 

def add_function(num1,num2):
    return num1+num2

result = add_function(1,2)

print(result)

def name_function():
    '''
    DOCSTRING: information about the function 
    input
    output: Hello 
    '''
    print('Hello')
    
name_function()

def say_hello(name = 'NAME'): #the equal sign assigns a default to the function
    return 'Hello '+ name #adding a return function 

result = say_hello('Rick') #add a variable value to the name 

result

#Method 2
def myfunc(name):
    print('Hello {}'.format(name))
    
myfunc('Lionel')

def add(n1,n2):
    return n1+n2

result = add(20,30)

result #saves the outcome as a variable name 

#Examples
# Find out if the word "dog" is in a string 

#Beginner
def dog_check(dogstring):
    if 'dog' in dogstring.lower():
        return True
    else:
        return False 
    
dog_check('my Dog ran away')

#Notice the boolean in logic
def dog_check(dogstring):
    return 'dog' in dogstring.lower()
    
dog_check('my cat ran away')

#Pig Latin
def pig_latin(word):
    
    first_letter = word[0] 
    
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

pig_latin('apple')

#Value of boolean
def myfunc_a(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

a = False 

result = myfunc_a(a)

result


def myfunc_b(x,y,z):
     if z == True: 
         return x
     else:
         return y

myfunc_b(1,2,False)

#Simple math
def myfunc_1(a,b):
    return a+b

myfunc_1(5,6)

#Even number
def is_even(n):
    if n%2 == 0:
        return True
    else: 
        return False
    
is_even(6)

#greater than
def is_greater(x,y):
    if x > y:
        return True
    else:
        return False

is_greater(6,7)

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
# if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
lesser_of_two_evens(102,98)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns 
# True if both words begin with same letter
def animal_crackers(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]
    
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy kangaroo')
    
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
# If not, return False

def makes_twenty(x,y):
    if x+y == 20:
        return True
    elif x == 20 or y == 20:
        return True
    else:
        return False 

makes_twenty(3,4)

#streamlined version
def makes_twenty1(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

makes_twenty1(5,6)

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
    
old_macdonald('mackinsey')

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return ' '.join(text.split()[::-1])

master_yoda('scientia sic potentia')

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#my solution
def almost_there(n):
    if 90<=abs(n)<=110 or 190<=abs(n)<=200: #doesn't really need an absolute value 
        return True 
    else:
        return False 
    
almost_there(95)

#proposed solution 
def almost_there_proposed(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)) 

almost_there_proposed(55)

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # alternative:
        #if nums[i:i+2] == [3,3]
    
        if nums[i] == 3 and nums[i+1] == 3:
            return True  
    
    return False

has_33([1,2,3,5])

#PAPER DOLL: Given a string, return a string where for every character in the original 
# there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

paper_doll('hello')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(x,y,z):
    
    if sum((x,y,z)) <= 21:
        return sum((x,y,z))
    elif sum((x,y,z)) <=31 and 11 in (x,y,z):
        return sum((x,y,z)) - 10
    else:
        return 'BUST'
    
blackjack(1,9,11)

blackjack(5,11,11)

blackjack(10,10,10)



#SUMMER OF '69: Return the sum of the numbers in the array, 
#except ignore sections of numbers starting with a 6 and extending to the next 9
#(every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([6,7,8,9])

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1

spy_game([1,2,4,0,0,7,5])
spy_game([1,7,2,0,4,5,0])
spy_game([1,0,2,4,0,5,7])
spy_game([1,0,0,5,7,8,9,10])

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  
        #The list starts at 3 and goes by 2s because 
        #it avoids any num divisible by 2
            if x%y == 0: #not a prime, if it finds any value of y for which x mod y is 0, then x it's not prime. 
                x += 2
                break
        else:
            primes.append(x) #prime number, if there is no y for which x mod y is 0, then it is a prime number
            x += 2
    print(primes)
    return len(primes)

count_primes(20)

#alternative
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

count_primes2(100)

#Is num a prime? 
def is_prime(num): 
    x = num 
    for y in range(3,x):
        if x%y == 0:
         return False
    else:
        return True
 
is_prime(15)


#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
        
print_big('a')

#*args (arguments) and **kwargs (keyword arguments)

def func1(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d,e))*0.05

func1(40,60)

def func2(*args): #allows inclusion of as many arguments as desired
    return sum(args) * 0.05
    
func2(40,60,70,100,2)

def func3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
        
func3(fruit = 'banana')

def func4(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
    
func4(10,20,30,fruit = 'oranges', food = 'eggs', animal = 'dog')

def myfunc2(*args):
    return [n for n in args if n%2 == 0]

myfunc2(1,2,3,4,5,6)

#function takes a string and returns even letters
#in upper case and odd in lower case

def myfunc3(x):
    out = []
    for i in range(len(x)): 
        if i%2==0: 
            out.append(x[i].lower())
            ## because an index starts at 0
        else:
            out.append(x[i].upper())
    return ''.join(out)

myfunc3('Anthropomorphism')

#Map function
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)
    
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Messi']

list(map(splicer,names))

#filter function
#filters the iterable objects in list 
# based on a previous defined function condition
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even,mynums):
    print(n)

list(filter(check_even,mynums)) #other way, create list 

#Lambda expression
def square(num):
    result = num**2
    return result

square(3)

lambda num: num**2 #same as above 

my_nums = [1,2,3,4,5,6]
list(map(lambda num: num**2,my_nums)) #no need to def func

list(filter(lambda num:num%2 == 0,my_nums))

names

list(map(lambda name:name[0],names))

list(map(lambda name:name[::-1],names))

#Nested statements and scope
x = 25

def printer():
    x = 50
    return x 

print(x)
print(printer())
 #LEGB rule
 #lambda num:num**2 num is a local variable, within a func
 name = 'This is a global string' #global variable (3rd)
 
 def greet():
     name = 'Sammy' #enclosing functions (2nd)
     
     def hello():
         name = 'Messi' #Local variable (1st)
         print('Hello '+ name)
     hello()
     
greet()

x = 50

def func(x):
    print(f'X is {x}')
    
    #Local reassignment
    x = 200
    print(f'I just locally changed x to be {x}')
    
func(x) #Takes local variable
print(x) #Takes the global variable

def func1():
    global x
    print(f'X is {x}')
    
    #Local reassignment on a global variable
    x = 200
    print(f'I just locally changed global x to be {x}')
    
func1()
print(x) #changed global value of variable

#Do this
def func1(x):
    print(f'X is {x}')
    
    #Local reassignment on a global variable
    x = 200
    print(f'I just locally changed global x to be {x}')
    return x
func1(x)
x = func1(x)
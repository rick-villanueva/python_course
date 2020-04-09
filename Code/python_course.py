
print("Hello World") 

#Section 3: Python Object and Data Structure Basics 
2+1

3/2

7 % 4 #Returns the remainder of a division 

23 % 2 #Check if this number (23) is odd (there's a remainder)

2 ** 3 #2 to the power of 3

2 + 10 * 10 + 3

(2 + 10) * (10 + 3) #Order of operations 

0.1 + 0.2 - 0.3

1/2

#Variable Assignments 
my_dogs = 2 

my_dogs = ["Sammy", "Frankie"]

print(my_dogs)

a = 5

a

a + a

a = a + a #adds the latest value of a

a

type(a)

a = 30.1

type(a)

my_income = 100

tax_rate = 0.1

my_taxes = my_income*my_taxes

my_taxes

#Strings 

"hello"
'this is a string'
"I'm going on a run"

print("hello")
print("hello world one")
print("hello world two")
print("hello \nworld") #\n for a new row
len("hello")

mystring = "Hello World"

mystring

mystring[0]

mystring[8]

mystring[-2]

mystring = "abcdefghijk"

mystring[2:]

mystring[:3] #The stop index means go up to but don't include the actual last number of the string

mystring[3:6]

mystring[1:3]

mystring[::]

mystring[::2] #steps

mystring[::3]

mystring[::-1] #reverse a string 

name = "Sam" #strings are inmutable

last_letters = name[1:]

last_letters

"P" + last_letters #The function for concatenate in python is + sign

x = "hello world"

x + " it is beautiful outside!"

x = x + " it is beautiful outside!"

x

letter = "z"

letter * 10

2 + 3

"2" + "3" #When concatenating strings, no operation is made

x = "Hello World"

#Methods in python
x.upper() 

x.lower()

x.split() #Split based on the white space

x = "this is a string"

x.split("i") #split based on a partial string

#String interpolation
my_name = "Rick"

my_name

print("this is a string {}".format("INSERTED")) #the .format function inserts the new string where the braces are 

print("the {2} {1} {0}".format("fox","brown","quick")) #Assigning the index to the braces 

print("the {q} {b} {f}".format(f = "fox",b = "brown", q = "quick")) #Assigning variables in index 

result = 100/777

result

print("The result was {r}".format(r=result))

#Float formatting follows "{value:width.precision f}"
print("The result was {r:1.3f}".format(r=result))

result_1 = 104.12345

print("The result was {r1:1.3f}".format(r1=result_1))

#f strings literal 
name = "Chris"

print(f"hello, his name is {name}")

name1 = "Sam"
age = 3

print(f"{name1} is {age} years old") 

my_list = [1,2,3]

my_list1 = ["String",100,23.2]

mylist = ["one", "two","three"]

mylist[0]

another_list = ["four", "five"]

mylist + another_list #concactenate two lists

new_list = mylist + another_list

new_list

new_list[0] = "ONE" #Change elements in a list 

new_list.append("six") #Add an object to the end of a list

new_list

new_list.append("seven")

new_list

new_list.pop() #Deletes last item of a list

new_list

popped_item = new_list.pop()

popped_item

new_list

new_list.pop(0) #Deletes a specific index 

new_list

new_list = ["a","e","x","b","c"]
num_list = [4,1,8,3]

new_list.sort() #sorts list in alphabetical order 

new_list

num_list.sort() #sorts lists in numerical order 

num_list

num_list.reverse() #Reverses de elements of a list

num_list

#Dictionaries

#Dictionarios are unordered and cannot be sorted. Objects retrieved by key name
#Lists retrieve objects by location. Can be indexed or sliced 

my_dictionary = {"key1":"value1","key2":"value2"}

my_dictionary["key1"]

prices_lookup = {"apples":2.99,"oranges":1.99,"milk":5.80}

prices_lookup["apples"]

d = {"k1":123,"k2":[1,2,3],"k3":{"insidekey":100}} #Dictionary within a dictionary

d["k2"]

d["k3"]["insidekey"] #Calling the element of a dictionary within a dictionary

d["k2"][1] #Calling an element of a list by index

e = {"key1":["a","b","c"]}

e

mylist = e["key1"]

mylist

letter = mylist[2]

letter

letter.upper()

e["key1"][2].upper() #Circumvent creating a new list and indexing in a single line of code

f = {"k1":100,"k2":200}

f["k3"] = 300 #Add a new value to a dictionary

f

f["k1"] = "NEW VALUE" #Change value to 

f

f = {"k1":100,"k2":200,"k3":300}

f.keys() #Returns all the keys

f.values() #Returns all the values

f.items() #Returns all the pairs

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} #Extreme example of calling a specific element

d['k1'][2]['k2'][1]['tough'][2][0]

#Tuples - like lists but immutable
t = (1,2,3)

l = [1,2,3]

type(t)
type(l)

tup = ("a","a","b")

tup.count("a")

tup.index("a")

tup

l

l[0] = "NEW"

l

tup[0] = "z" #Cannot change an element in a tuple

#Sets - unordered collection of unique elements (cannot repeat element)
myset = set()

myset.add(1)

myset

myset.add(2)

myset

myset.add(2) #Cannot add a value already in the set 

mylist = (1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3)

set(mylist)

#Booleans - Convey either true or false statements
1 > 2 #Comparison operators

1 == 1

#Files
fh = open("demo.txt","w")

fh.write("Leo Messi es el mejor jugador del mundo")
fh.close()

fh = open("demo.txt","a")

fh.write("\nCristiano #2")
fh.close()

mylist = "2"

mylist

type(mylist)

type(3 + 1.5 + 4)

#Section 2: Python Comparison Operator
2 == 2 

2 == 1

'hello' == 'bye'

'bye' == 'Bye' #capitalization counts 

3 != 3 #Not equal to sign !=

4 != 5

2 > 1

2>= 4 #Greater than or equal to 

#Logical operators
1 < 2 
2 < 3
1 < 2 < 3
1 < 2 > 3

1 < 2 and 2 > 3 #change the chain for a logical operator 

('h' == 'h') and (2 ==2) #Parenthesis not needed but common practice

(1 == 1) or (2 == 2)

(1 == 3) or (2 == 2) #Only needs one statement to be true 

not (1 == 1)

#Section 3:Python statements
#control flow allows to operate just a specific part of code


hungry = False
if hungry:
    print("Feed Me")
else:
    print("I'm not hungry")

a = 1

if a == 1:
    print('OK')
else:
    print("Check")
    
loc = "Store"

if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "Store":
    print("Welcome to the store")
else:
    print("Not know")
    
name = "Messi"

if name == "DeJong":
    print("Best Mid")
elif name == "Suarez":
    print("Best 9")
elif name == "Messi":
    print("The Goat")
else: 
    print("FCB")

#Loops
#for loops 
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
    
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    print(num)

my_list = [1,2,3,4,5,6,7,8,9,10]
for Messi in my_list: 
    print("Messi") #prints out the string 10x
    
for num in my_list:
    if num % 2 == 0: #check even numbers
        print(num)
    else:
        print(f"odd num:{num}")
        
list_sum = 0 

for num in my_list:
    list_sum = list_sum + num #For every num in my_list, start with original sum = 0 and add the num
    
print(list_sum) #Identation of this kind gives only the final #

mystring1 = "Hello World"

for letter in mystring1: 
    print(letter)
    
tup = (1,2,3)

for item in tup:
    print(item)

mylist5: [(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist5: #tuple unpacking
    print(a)
    print(b)

mylist6 = [(1,2,3),(5,6,7),(8,9,10)]

for a,b,c in mylist6:
    print(b) #print middle num

d = {"k1":1,"k2":2,"k3":3} #iterate through a

for item in d:
    print(item) #calls the keys
    
for item in d.items():
    print(item) #calls values
    
for a,b in d.items():
    print(b)

#While Loops
x = 0 

while x < 5:
    print(f"The current value of x is {x}")
    x = x +1 #limits how many times it runs by the logic in while loop 
else:
    print("x is not less than 5")
    #Other way to write x += 1 

y = [1,2,3]

for item in y:
    pass #allows the for loop to not run

string1 = "Messi"

for letter in string1:
    if letter == "e":
        continue
    print(letter)
    
for letter in string1:
    if letter == "e":
        break #stops the loop
    print(letter)
    
x = 0 

while x < 5:
    if x == 2:
        break
    print(x)
    x = x + 1 
    
x = 2 

while x < 10:
    if x == 7:
        break
    print(x)
    x = x + 1
    
#Operators 
for num in range(10):
    print(num)
    
for num in range(0,11,2):
    print(num)
    
list(range(0,11,2))

index_count = 0 

for letter in "abcde":
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1 
 
index_count = 0    
word = "abcde"

for letter in word:
    print(word[index_count])
    index_count += 1 

word = "abcde"

for item in enumerate(word):
    print(item)
    
    
word = "abcde"

for index,letter in enumerate(word): #the enumerate function returns the elements of an element 
    print(index)
    print(letter)
    print("\n")
    
alist1 = [1,2,3]
alist2 = ["a","b","c"]

for item in zip(alist1,alist2):
    print(item)
    
alist1 = [1,2,3]
alist2 = ["a","b","c"]
alist3 = [100,200,300]

for item in zip(alist1,alist2,alist3):
    print(item)
    
"x" in [1,2,3] #in operator

2 in [1,2,3]

"a" in "a world"

"mykey" in {"mykey":345}

d = {"mykey":345}

345 in d.values()
345 in d.keys()

numbers = [10,20,30,40,50,100]

min(numbers)

max(numbers)

from random import shuffle #shuffle func (must be imported)

numeros = [1,2,3,4,5,6,7,8,9,10]

shuffle(numeros)

numeros

from random import randint #random integer func 

randint(0,100)

mynum = randint(0,1000)

mynum

input 

result = input("Name: ")

result

fav_num = input("Favorite Number: ")

fav_num #brings back a string

int(fav_num) #to bring back as integer 

float(fav_num) #to bring back as float

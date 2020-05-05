#Generators
def create_cubes(n):
    for x in range(n):
        yield x**3
    
list(create_cubes(11)) 

for x in create_cubes(11):
    print(x)
    
#Fibonacci
def gen_fibonacci(n):
    a = 1 
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for num in gen_fibonacci(10):
    print(num)
    
#Next function
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

#Iter functions
s = 'hello'

s_iter = iter(s)

next(s_iter)
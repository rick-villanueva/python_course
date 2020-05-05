def hello(name='Messi'):
    print('The hello function has been executed')
    
    def greet():
        return '\t this is the greet function inside hello'

    def welcome():
        return '\t This is welcome inside hello'
    
    if name == 'Messi':
        return greet()
    else:
        return welcome()
    
hello()
    
myfunc = hello('Messi')

myfunc #only returns the greet function inside hello()

print(myfunc)

#Example
def cool():
    
    def super_cool():
        return 'I am very cool'
    
    return super_cool()

some_func = cool()

some_func


#Passing a function as an argument
def saludo():
    return 'Hi Rick'

def other(some_def_func):
    print('Other code runs')
    print(some_def_func())

other(saludo) #The func is an argument and the other func executes saludo

#Decorator
def new_decorator(original_func):
    
    def wrap_func():
        print('Some extra code, before the original_func')
        
        original_func()
        
        print('Some extra code, after the original_func')
        
    return wrap_func() #Returns the wrapped version of original_func

@new_decorator
def decorated_func():
    print('I want to be decorated')

decorated_func

    



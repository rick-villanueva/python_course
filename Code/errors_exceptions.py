def add(n1,n2):
    print(n1+n2)
    
add(10,20)

number1 = 10
number2 = input('Please provide a number: ')

add(number1,number2)

#Try,except,else
try:
    #Code to attempt
    result = 10 + 'Messi'
except:
    print('Not adding correctly')
else: 
    print('Addition result')
    print(result)
    
result


#Try,except,finally
try:
    f = open('testfile','w')
    f.write('Write a test line')
except TypeError:
    print('Error Found')
except OSError:
    print('OS Error found')
finally:
    print('I always run')


#Most common syntax
try:
    f = open('testfile','w')
    f.write('Write a test line')
except:
    print('Error Found')
finally:
    print('I always run')
    
#example
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Not a number')
            continue
        else:
            break
        finally:
            print('End of iteration')
        
ask_for_int()


#HW prob
def ask_squared():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)
    
ask_squared()
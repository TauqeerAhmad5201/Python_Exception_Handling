# try - else 
try:
    a = int(input('Please enter the number 1:- '))
    b = int(input('Please enter the number 2:- '))
    c = a+b 
    d = a*b 
    e = a/b 
except ValueError: 
    print('Please use integer value.')
except NameError: 
    print('The value has not been defined.') 
except TypeError: 
    print('Try to work with similar data type')
except ZeroDivisionError: 
    print('Try to provide number greater than 0 (Zero)')
except Exception as ex:
    print(ex + ' has been occured')
else:
    print(c)
    print(d)
    print(e)
finally: 
    print('Execution has been done')
'''
whatever our main approach of the program is, should be written in the else part of the try 
'''
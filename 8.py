'''By raising the error using 'raise' keyword, one can easily raise their desired error type with a statement 
'''


#Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError('Only integers required.')

#Raise an error and stop the program if y is lower than 0:
y =  -1 

if y < 0: 
    raise Exception('Provide value greater than 0')
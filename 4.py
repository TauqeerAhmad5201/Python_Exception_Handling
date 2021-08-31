a = 5 
b = 0 

print('Starting')
try: 
    print(a/b)
except ZeroDivisionError as z: 
    print('Sorry, this is illegal.')

try:
    k = int(input('Enter an integer'))
except ValueError as v: 
    print('Sorry, you have not entered the required value')
finally: 
    print('He we are :-')
    

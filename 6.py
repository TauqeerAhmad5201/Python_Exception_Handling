''' Always a good practice to try and except in functions.
'''

try: 
    age = int(input('Enter the age please.'))
except: 
    print('You have given a wrong input')
else: 
    if age<=17:
        print('You\'re not eligible')
    else: 
        print('Okay!, You\'re eligible')

'''
whatever our main approach of the program is, should be written in the else part of the try 
'''
a = 5 
b = 2

print('Resource Open')
try:
    print(a/b)
    k = int(input('Enter a number\n '))
except ZeroDivisionError as z:
    print('Hey you cannot divide a number by zero Error Occur: ',z)
except ValueError as v: 
    print('Invalid Input',v)
except Exception as e:
    print('Something went wrong')
finally: 
    print('He we are :>')            

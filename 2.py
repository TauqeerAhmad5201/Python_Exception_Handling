try: 
    print('Statement 1')
    print(10/0)
    print('Statement 2')  #this line will not run because as soon the exception occurs, the controls moves over the except block
except: 
    print('Sorry 10/0 cannot be solved.')
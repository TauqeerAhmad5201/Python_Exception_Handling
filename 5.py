def divide(x,y):
    try: 
        result = x//y
    except ZeroDivisionError as z: 
        print('Sorry you cannot divide by zero. ',z)
    else: 
        print('Result : ',result)
    finally: 
        print('I think we have done it.')

divide(8,6)
divide(7, 0)

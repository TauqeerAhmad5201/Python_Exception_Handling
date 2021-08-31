''' The assert statement is useful that a given condition is True. If it is not true, it raises Assertion error.'''
# a = 10 
# assert a<=10, 'Invalid Number'

# here the condition is true, so the message is not gonna print.print

def get_age(age):
    assert age > 0, 'Age can not be negative'
    print(' OK ! ', age)
get_age(-1)
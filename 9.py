year = int(input('Please enter your year of birth :- '))
age = 2021 - year

class Error(Exception):
    pass 
class dobException(Error):
    pass
try: 
    if age<=30 & age>=20:
        print('Eligible')
    else: 
        raise dobException
except dobException:
    print('You cannot apply for exams.')
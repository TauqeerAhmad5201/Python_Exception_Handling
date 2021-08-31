'''  Custom exception --> we just create class with exception name and raise the error. Here we inherit that class from Exception class as a super class
'''
# class CoffeeCup: 
#     def __init__(self,temperature): 
#         self.temperature = temperature
    
#     def drink_coffee(self):
#         if self.temperature > 30:
#             raise Exception('Coffee too hot.')
#         elif self.temperature < 10: 
#             raise Exception('Coffee too cold')
#         else: 
#             print('OK ! Have your drink')
        
# c1 = CoffeeCup(9)
# c1.drink_coffee()
class CoffeeTooColdException(Exception):
    def __init__(self,msg):
        super().__init__(self,msg)

class CoffeeTooHotException(Exception):
    def __init__(self,msg):
        super().__init__(self,msg)

class CoffeeCup: 
    def __init__(self,temperature): 
        self.temperature = temperature
    
    def drink_coffee(self):
        if self.temperature > 30:
            raise CoffeeTooHotException('Coffee too hot.')
        elif self.temperature < 10: 
            raise CoffeeTooColdException('Coffee too cold')
        else: 
            print('OK ! Have your drink')
        
c1 = CoffeeCup(9)
c1.drink_coffee()
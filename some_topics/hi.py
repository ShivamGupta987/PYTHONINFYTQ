# arr = [1,2,3]

# for i in arr:
  
#     if i == arr[-1]:
#         arr.pop()
#         i = i +1
#         print(i)

class ATMCard:
    def __init__(self, card_number, initial_password):
        self.card_number = card_number
        self._password = set()  
        self.set_password(initial_password)
        
          
    def _set_password(self, password):
      
        if self._is_valid_password(password):
            self.__password = password
        else:
            raise ValueError("Password must be at least 4 characters long.")
        
        
class ATM:
    def __init__(self, pin):
        self._pin = pin 
    def set_pin():
        pass 
        

    
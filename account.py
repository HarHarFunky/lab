class Account():
    def __init__(self,name: str):
        self.__account_name = name
        self.__account_balance = 0 # Cause you're broke
    def deposit(self, ammount):
        if ammount > 0:
            self.__account_balance+=ammount
            
            
            return True
        return False
    def withdraw(self, ammount):
        if ammount > 0:
            if ammount <= self.__account_balance:
                self.__account_balance-=ammount
                return True
        return False
    def get_balance(self): return self.__account_balance
    def get_name(self): return self.__account_name

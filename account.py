class Account():
    def __init__(self,name):
        self._account_name = name
        self._account_balance = 0 # Cause you're broke
    def deposit(self, ammount):
        if ammount > 0:
            self._account_balance+=ammount
            
            
            return True
        return False
    def withdraw(self, ammount):
        if ammount > 0:
            if ammount <= self._account_balance:
                self._account_balance-=ammount
                return True
        return False
    def get_balance(self): return self._account_balance
    def get_name(self): return self._account_name

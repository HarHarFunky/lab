class Account():
    def __init__(self,name: str):
        '''
        This is the initializer for the entire class
        :param name: This is what you will call the account
        '''
        self._account_name = name
        self._account_balance = 0 # Cause you're broke
    def deposit(self, ammount: float):
        '''
        This is a function to add money to your account
        :param ammount: How much money do you want to add?
        '''
        if ammount > 0:
            self._account_balance+=ammount
            
            
            return True
        return False
    def withdraw(self, ammount: float):
        '''
        This is a function to take money from your account
        :param ammount: How much money do you want to take?
        '''
        if ammount > 0:
            if ammount <= self._account_balance:
                self._account_balance-=ammount
                return True
        return False
    def get_balance(self):
        '''
        Get your account balance
        '''
        return self._account_balance
    def get_name(self):
        '''
        Get the account name
        '''
        return self._account_name

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        # self.__balance = 0
    def deposite(self , amount):
        
        self.__balance += amount
    def withdraw(self , withdraw_amount):

        amount = self.__balance - withdraw_amount

        self.__balance = amount
        if amount > 0 :
            return ("u can withdraw money ")
            
        else:
            return ("insufficent amount ")
        
    def get_balance(self):
        return self.__balance
        ...
    
a = BankAccount(1000)
a.deposite(500)

print(a.withdraw(100))

print(a.get_balance())



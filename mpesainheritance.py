class Account:
    def __init__(self, account_holder, balance):
        self.account_holder= account_holder
        self.balance= balance

    def deposit(self,amount):  #a function to deposit
        if amount >0:
            self.balance+=amount
            print(f"{amount} deposited successfully. New balance is {self.balance}")
        else:
            print("Amount should be greater than zero")

    def withdraw(self,amount):   #a function to withdraw
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(f"{amount} withdrawn successfully. New balance is {self.balance}")

    def __str__(self):
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}"


    #create a saving account
class SavingsAccount(Account):
    def __init__(self,account_holder, balance, interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate= interest_rate                #this is because interest_rate was not inherited
    def add_interest(self):
        interest= self.balance * self.interest_rate/100
        self.balance+=interest
        print(f"Interest added successfully. New balance is {self.balance}")

    def __str__(self):                                                   #this is an overide function
        return f"Savings Account holder:{self.account_holder}\nBalance: {self.balance},interest rate: {self.interest_rate}"
#CREATE OBJECTS
account= Account("George Okubi", 1000)
account.deposit(800)
account.withdraw(500)

print(account.balance)

savings= SavingsAccount("John Doe", 1000, 0.05)
savings.deposit(500)
savings.withdraw(500)
savings.add_interest()
print(savings)
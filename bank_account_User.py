class BankAccount:

    def __init__(self, balance = 0, rate = 0):  # Initialize class attributes
        self.balance = balance
        self.rate = rate

    def deposit(self, amount):  # Method to add funds to account
        self.amount = amount
        self.balance += self.amount
        return self

    def withdraw(self, amount): # Method to withdraw funds from account
        self.amount = amount
        if BankAccount.total_funds(self.balance, self.amount) == True:  # Checking if balance is bigger or same of amount to withdraw using total_funds() function
            self.balance -= amount
        else:
                print(f"Not enough funds to withdraw {self.amount}")
        return self

    def display_account_info(self): # Method to display account info
        print(f"Your balance is {self.balance}")
        return self

    def yield_interest(self):   # Method to add yield interest to balance
        if BankAccount.total_funds(self.balance, 0) == True:
            self.balance = self.balance + (self.balance * self.rate)
        else:
                print("Not enough funds to yield interest")
        return self

    @staticmethod                   
    def total_funds(funds, amount): # Static method to check if balance is same or more than 0 (True) or less than 0 (False) 
        if funds >= amount:
            return True
        else:
            return False


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(700, 0.05)
    
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()

user_001 = User("Gordo", "gordo@gmail.com")
print(user_001.name, user_001.email, user_001.account.balance)
user_001.deposit(500).withdraw(100).display_user_balance()

        

    
        

# galindo = BankAccount(100, 0.04)
# galindo.deposit(500).deposit(100).deposit(400)
# galindo.withdraw(600)
# galindo.display_account_info()



# luis = BankAccount(1000, 0.02)
# luis.deposit(1000).deposit(600).withdraw(100).withdraw(400).withdraw(1000).withdraw(400).yield_interest().display_account_info()

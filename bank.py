class Account:
    school="AkiraChix"
    def __init__(self,account_name,account_number,password,balance):
        self.account_name=account_name
        self.account_number=account_number
        self.password=password
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return self.balance


    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        return f"You've withdrawn {self.balance} on the {self.account_name} {self.account_number} "




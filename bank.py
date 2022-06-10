
class Account:
    school="AkiraChix"
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]



       

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount must be greater than zer"

        else:
            self.balance+=amount
            self.deposits.append(amount)


            return f"{self.balance}"

       
     
#condition for withdrawal to be succesful
#required amount must be greater than amount balance
    def withdrawal(self,amount):
        
        if amount > self.balance:
            return f"Insufficient funds"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance}"

    def deposit_history(self):
        for history in self.deposits:
            print(f"you have deposited {history}")


    def withdrawals_history(self):
      
        for withdraw in self.withdrawals:
            print(f"you have withdrawn {withdraw}")


    def withraw(self, amount):
        if amount > 0:
            self.balance-=amount+100
            return f"Hello {self.account_name}, you have withdrawn {amount} and your new balance is {self.balance}"
        elif amount <=0:
            return f"withdraw amount must be greater than zero"

        elif amount == self.balance:
            return f"Insuficient funda"

        else:
            return f"insuficient funds"

    def current_balance(self):
        return f"The current balance is KSH {self.balance}"


    


            

       



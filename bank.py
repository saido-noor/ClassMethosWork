from datetime import datetime
class Account:
    school="AkiraChix"
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction_cost=100
        self.loan_balance = 0



       

    def deposit(self,amount):
        self.balance+= amount
        self.deposits.append(amount)
        if amount <=0:
            return f"Deposit amount must be greater than zer"

        else:
            self.balance+=amount
            deposit_hist={"date":datetime.now().strftime('%d/%m/%y'),"amount":amount,"narration":f"You have succesfully deposited {amount} on {datetime.now()} "}
            self.deposits.append(deposit_hist)


            return f"{self.balance}"

       
     
#condition for withdrawal to be succesful
#required amount must be greater than amount balance
    def withdrawal(self,amount):
        self.balance -= amount
        self.withdrawals.append(amount)
        if amount > self.balance:
            return f"Insufficient funds"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            withdrawal_hist={"date":datetime.now().strftime('%d/%m/%y'),"amount":amount,"narration":f"ou have withdrawn {amount} on {datetime.now()} "}
            self.withrawals.append(withdrawal_hist)
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance}"

    def deposit_history(self,amount):
       

        for history in self.deposits:
            print(f"you have deposited {history}")


    def withdrawals_history(self,amount):
       
        for withdraw in self.withdrawals:
            print(f"you have withdrawn {withdraw}")


    def withraw(self, amount):
        withrawable_balance = self.balance-self.transaction_cost
#if amount+self.transactioncost>self.balance
        if amount > withrawable_balance:
            # self.balance-=amount+self.transaction_cost
            return f"Hello {self.account_name}, you have withdrawn {amount} and your new balance is {self.balance}"
        elif amount <=0:
            return f"withdraw amount must be greater than zero"

        elif amount == self.balance:
            return f"Insuficient funda"

        else:
            return f"insuficient funds"

    def current_balance(self):
        return f"The current balance is KSH {self.balance}"


    def full_statement(self):
        statement=self.deposits+self.withrawals
        for a in statement:
            if a in self.deposits:
                print(f"{a['date']}_____deposit____-{a['amount']} ")
            elif a in self.withrawals:
                print(f"{a['date']}_____withrawal____ {a['amount']}" )
           
    def borrow(self,amount):
        deposit_sum=0
        for a in self.deposits:
            deposit_sum+=a["amount"]
        if amount<=0:
            return "invalid amount"
        if len(self.deposits)<10:
            return f"Your borrow must be greater than make {10-len(self.deposits)} more deposits to qualify"
        if amount<100:
            return "You can borrow 100ksh"
        if self.balance!=0:
            return f"You have {self.balance} KSH in your balance. Your balance must be equal to zero"
        if amount> deposit_sum/3:
            return f"You are not qualified to borrow this amount. You can borrow atmost {deposit_sum/3}"
        if self.loan_balance!=0:
            return f"YOu have unpaid loan of {self.loan_balance}, for you to borrow first pay the loan that you have"
        else:
            interest=(3/100)*amount
            self.loan_balance+=amount+interest
            return f"You have borrowed {amount} the loan to be paid is equal to {self.loan_balance}"
    def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            remainder=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(remainder)}"
        else:
            self.loan_balance-=amount
            return f"You have paid a loan of {amount} KSH and your current loan balance is {self.loan_balance} "
    def transfer(self,amount,instance_name):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return "insufficient amount"
        else:
            self.balance-=amount
            instance_name.balance+=amount
            return f"You have transfered {amount} KSH to the account with the name of {instance_name.account_name}. Your new balance is {self.balance}"



    


            

       



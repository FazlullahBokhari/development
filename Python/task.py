class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return f"Name of account holder:{self.owner}, Current balance : {self.balance}"
    def deposite_money(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(dep_amt," deposited")
    def withdraw_money(self,wd_amt):
        if self.balance > wd_amt:
            self.balance = self.balance - wd_amt
            print(wd_amt," credited")
        else:
            print("balance insufficient")
    def __len__(self):
        return self.balance

acc = Account("Faiz",14000)
acc.deposite_money(29000)
acc_balance = len(acc)
print(acc_balance)
print(acc)
acc.withdraw_money(19000)
acc_balance = len(acc)
print(acc_balance)
print(acc)
acc.withdraw_money(50000)

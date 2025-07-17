#Bank Account Transaction Details#
class Account:
    def __init__(self,name,acc_no,acc_bal):
        self.name=name
        self.acc_no=acc_no
        self.acc_bal=acc_bal
    def debit(self,amount):
        self.acc_bal -= amount
        print(f"Rs.",amount,"was Debited.")
        print("Current Balance is:",self.get_balance())
       
    def credit(self,amount):
        self.acc_bal += amount
        print(f"Rs.",amount,"was Credited.")
        print("Current Balance is :",self.get_balance())
       
    def get_balance(self):
       return self.acc_bal

p1=Account("Hruta",93242757,5000)
print("Account Holder Name:",p1.name)
print("Account Number:",p1.acc_no)
print("Account Balance:",p1.acc_bal)   
p1.debit(1000)
p1.credit(2000)




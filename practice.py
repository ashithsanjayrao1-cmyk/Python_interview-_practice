class Account: 
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        if amount > self.balance:
            print("Inssuficient money",amount)
            print("Total balance is = ", self.get_balance())
        else:
            self.balance -= amount
            print("Rs.",amount,"was debited")
            print("Total balance is = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount,"was credited")
        print("Total balance is = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(100, 1245)
acc1.debit(2200)
acc1.credit(500)


         
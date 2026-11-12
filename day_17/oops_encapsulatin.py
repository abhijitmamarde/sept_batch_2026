# Encapsulation
# Encapsulation, the design / approach we choose to hide the important data attributes AND methods
# DA -> we dont care or have exposure that any method works on which data attributes

class Account:
    balance = 0

    # credit(amount)
    def credit(self, amount, type_txn="CD", txn_source_details=None):
        if type_txn == "CD" and amount > 50000:
            if txn_source_details is None:
                txn_source_details = input("What is the source of this cash amount?")
        
        self.balance += amount

    def get_current_balance(self):
        print("Balance is:", self.balance)
        

a1 = Account()
a2 = Account()
a3 = Account()

a1.credit(50001, "DD")
a1.get_current_balance()

a2.credit(50001, "CD")
a2.get_current_balance()

a3.credit(50001, "CD", "Got Annual Bonus")
a3.get_current_balance()

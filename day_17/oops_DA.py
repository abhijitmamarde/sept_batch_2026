# DA - Data Abstraction

# this is global state variable
# this is public / used by all the relevant functions
account_amount = 3000

def debit(db_amount, type_of_account):
    global account_amount
    if type_of_account == "CA":
        if (account_amount - db_amount) > -10000:
            account_amount -= db_amount
            return True, account_amount
        else:
            return False, account_amount

class CommonAccountType:

    def __init__(self, initial_account_balance=0) -> None:
        self._account_amount = initial_account_balance

    def get_current_balance(self):
        print(f"Current account balance is:", self._account_amount)

class SavingsAccount(CommonAccountType):

    def debit(self, db_amount):
        if (self._account_amount - db_amount) > 0:
            self._account_amount -= db_amount
            return True
        else:
            return False

class CurrentAccount(CommonAccountType):

    def debit(self, db_amount):
        if (self._account_amount - db_amount) > -10000:
            self._account_amount -= db_amount
            return True
        else:
            return False

sa = SavingsAccount(1000)

ca = CurrentAccount()

if sa.debit(1):
    print(f"Debit was successfull...")
sa.get_current_balance()

ca.debit(1999)
ca.get_current_balance()


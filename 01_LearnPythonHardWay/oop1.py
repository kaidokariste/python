# Tutorial from http://anandology.com/python-practice-book/object_oriented_programming.html

class BankAccount(object):

    money_in_bank = 100000

    def __init__(self, initialsaldo):
        self.balance = initialsaldo

    # Object balance amount minus, bank account plus
    def withdraw(self, amount):
        self.balance -= amount
        BankAccount.money_in_bank += amount
        return self.balance

    #object balance amount plus bank account minus
    def deposit(self,amount):
        self.balance += amount
        BankAccount.money_in_bank -= amount
        return self.balance

# Kaido opened a new account in bank meaning we defined
# object kaidoaccount
kaidoaccount = BankAccount(1200)
# we used overall bank money to make a deposit in kaido account
kaidoaccount.deposit(550)

# the balance of kaidoaccount is now 550 and overall 99450
print('Kaido balance after deposit', kaidoaccount.balance)
print('Money in bank after Kaido deposit', kaidoaccount.money_in_bank)

# Jim opened also bank account
jimaccount = BankAccount(2000);
print('Money currently in bank', jimaccount.money_in_bank)

# Jim pays back loan
jimaccount.withdraw(1400)
print('Jim balance after withdraw {}'.format(jimaccount.balance))
print('Money in bank after jim payment {}'.format(jimaccount.money_in_bank))

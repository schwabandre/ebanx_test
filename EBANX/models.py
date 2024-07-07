#Em memória "Banco de dados"
class Account:
    def __init__(self, account_id, balance = 0):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def transfer(self, amount, destination_account):
        if self.withdraw(amount):
            destination_account.deposit(amount)
            return True
        return False


accounts = {}

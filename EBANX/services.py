#Contém lógica de negócios para operações com contas e transações

from models import Account

accounts = {}

def reset_system():
    global accounts
    accounts = {}

def get_balance(account_id):
    account = accounts.get(account_id)
    if account:
        return account.balance
    return None

def deposit(destination, amount):
    account = accounts.get(destination)
    if not account:
        account = Account(destination, amount)
        accounts[destination] = account
    else:
        account.balance += amount
    return {"destination": {"id": account.id, "balance": account.balance}}, 201

def withdraw(origin, amount):
    account = accounts.get(origin)
    if not account:
        return 0, 404
    if account.balance < amount:
        return {"message": "Insufficient funds"}, 400
    account.balance -= amount
    return {"origin": {"id": account.id, "balance": account.balance}}, 201

def transfer(origin, destination, amount):
    origin_account = accounts.get(origin)
    destination_account = accounts.get(destination)
    if not origin_account:
        return 0, 404
    if origin_account.balance < amount:
        return {"message": "Insufficient funds"}, 400
    if not destination_account:
        destination_account = Account(destination, 0)
        accounts[destination] = destination_account
    origin_account.balance -= amount
    destination_account.balance += amount
    return {
        "origin": {"id": origin_account.id, "balance": origin_account.balance},
        "destination": {"id": destination_account.id, "balance": destination_account.balance}
    }, 201

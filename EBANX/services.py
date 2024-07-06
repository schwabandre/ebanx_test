#Contém lógica de negócios para operações com contas e transações

from models import accounts

def reset():
    global accounts
    accounts = {}

def get_balance(account_id):
    if account_id in accounts:
        return accounts[account_id], 200
    else:
        return {"error": "Account not found/Conta nao encontrada"}, 404
    
def deposit(destination, amount):
    if destination not in accounts:
        accounts[destination] = 0
    accounts[destination] += amount
    return {'id': destination, 'balance': accounts[destination]}, 201

def withdraw(origin, amount):
    if origin not in accounts:
        return {"error": "Account not found/Conta nao encontrada"}, 404
    if accounts[origin] < amount:
        return {"error": "Insufficient funds/Saldo insuficiente"}, 400
    accounts[origin] -= amount
    return {'id': origin, 'balance': accounts[origin]}, 201

def transfer(origin, destination, amount):
    if origin not in accounts:
        return {"error": "Origin account not found/Nao foi possível encontrar a origem da conta"}, 404
    if accounts[origin] < amount:
        return {"error": "Insufficient funds/Saldo insuficiente"}, 400
    if destination not in accounts:
        accounts[destination] = 0
    accounts[origin] -= amount
    accounts[destination] += amount
    return {
        'origin': {'id': origin, 'balance': accounts[origin]},
        'destination': {'id': destination, 'balance': accounts[destination]}
    }, 201
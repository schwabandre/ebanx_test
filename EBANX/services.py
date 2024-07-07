#Contém lógica de negócios para operações com contas e transações

from models import Account, accounts

def reset_system():
    global accounts
    accounts = {}

def get_balance(account_id):
    account = accounts.get(account_id)
    if account:
        return account.balance
    return None

def create_event(event_data):
    event_type = event_data.get('type')
    if event_type == 'deposit':
        destination = event_data.get('destination')
        amount = event_data.get('amount')
        if destination not in accounts:
            accounts[destination] = Account(destination)
        accounts[destination].deposit(amount)
        return {"destination": {"id": destination, "balance": accounts[destination].balance}}
    
    elif event_type == 'withdraw':
        origin = event_data.get('origin')
        amount = event_data.get('amount')
        if origin in accounts and accounts[origin].withdraw(amount):
            return {"origin": {"id": origin, "balance": accounts[origin].balance}}
        return {"message": "Insufficient funds or account not found"}
    
    elif event_type == 'transfer':
        origin = event_data.get('origin')
        destination = event_data.get('destination')
        amount = event_data.get('amount')
        if origin in accounts:
            if destination not in accounts:
                accounts[destination] = Account(destination)
            if accounts[origin].withdraw(amount):
                accounts[destination].deposit(amount)
                return {
                    "origin": {"id": origin, "balance": accounts[origin].balance},
                    "destination": {"id": destination, "balance": accounts[destination].balance}
                }
        return {"message": "Insufficient funds or account not found"}

    return {"message": "Invalid event type"}

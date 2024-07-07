#Ponto de entrada da aplicação Flask e usará os serviços definidos em 'services.py'

from flask import Flask, request, jsonify
from services import reset_system, get_balance, deposit, withdraw, transfer

app = Flask(__name__)

@app.route('/reset', methods=['POST'])
def reset():
    reset_system()
    return 'OK', 200

@app.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')
    balance = get_balance(account_id)
    if balance is None:
        return '0', 404
    return str(balance), 200

@app.route('/event', methods=['POST'])
def event():
    data = request.json
    event_type = data.get("type")

    if event_type == "deposit":
        destination = data.get("destination")
        amount = data.get("amount")
        result, status_code = deposit(destination, amount)
        return jsonify(result), status_code

    elif event_type == "withdraw":
        origin = data.get("origin")
        amount = data.get("amount")
        result, status_code = withdraw(origin, amount)
        return jsonify(result), status_code

    elif event_type == "transfer":
        origin = data.get("origin")
        destination = data.get("destination")
        amount = data.get("amount")
        result, status_code = transfer(origin, destination, amount)
        return jsonify(result), status_code

    return '0', 400

if __name__ == '__main__':
    app.run(debug=True)

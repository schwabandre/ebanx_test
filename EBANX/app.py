#Ponto de entrada da aplicação Flask e usará os serviços definidos em 'services.py'

from flask import Flask, request, jsonify
from services import reset, get_balance, deposit, withdraw, transfer

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the EBANX Challenge API!"

@app.route('/reset', methods=['POST'])
def reset_route():
    reset()
    return '', 200

@app.route('/balance', methods=['GET'])
def get_balance_route():
    account_id = request.args.get('account_id')
    balance, status = get_balance(account_id)
    if status == 200:
        return jsonify(balance), status
    else:
        return jsonify(balance), status

@app.route('/event', methods=['POST'])
def event_route():
    data = request.json
    event_type = data.get('type')

    if event_type == 'deposit':
        destination = data.get('destination')
        amount = data.get('amount')
        response, status = deposit(destination, amount)
        if status == 201:
            return jsonify({'destination': response}), status
        else:
            return jsonify(response), status

    elif event_type == 'withdraw':
        origin = data.get('origin')
        amount = data.get('amount')
        response, status = withdraw(origin, amount)
        if status == 201:
            return jsonify({'origin': response}), status
        else:
            return jsonify(response), status

    elif event_type == 'transfer':
        origin = data.get('origin')
        amount = data.get('amount')
        destination = data.get('destination')
        response, status = transfer(origin, destination, amount)
        if status == 201:
            return jsonify(response), status
        else:
            return jsonify(response), status

    return jsonify({"error": "Invalid event type/Evento invalido"}), 400

if __name__ == '__main__':
    app.run(debug=True)
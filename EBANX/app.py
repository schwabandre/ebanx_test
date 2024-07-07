#Ponto de entrada da aplicação Flask e usará os serviços definidos em 'services.py'

from flask import Flask, request, jsonify
from services import reset_system, get_balance, create_event

app = Flask(__name__)


@app.route('/reset', methods=['POST'])
def reset():
    reset_system()
    return jsonify({"message": "System reset successful"}), 200

@app.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')
    balance = get_balance(account_id)
    if balance is None:
        return jsonify({"message": "Account not found"}), 404
    return jsonify({"balance": balance}), 200

@app.route('/event', methods=['POST'])
def event():
    event_data = request.get_json()
    result = create_event(event_data)
    if 'message' in result:
        return jsonify({"message": result['message']}), 404
    return jsonify(result), 201

if __name__ == '__main__':
    app.run(debug=True)

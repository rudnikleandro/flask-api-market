from flask import Flask, request, jsonify
from services.stocks import get_stock_data
from services.crypto import get_crypto_data

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API de Cotações"})

@app.route("/stocks", methods=["GET"])
def stocks():
    ticker = request.args.get("ticker")
    if not ticker:
        return jsonify({"error": "o parâmetro 'ticker' é obrigatório"}), 400
    
    data = get_stock_data(ticker)
    return jsonify(data)

@app.route("/crypto", methods=["GET"])
def crypto():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "O parâmetro 'sumbol' é obrigatório"}), 400
    
    data = get_crypto_data(symbol)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
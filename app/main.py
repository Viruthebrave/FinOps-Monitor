from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Welcome to FinOps Monitor</h2>
    <p>Check live finance data:</p>
    <ul>
        <li>/stock/AAPL → Apple stock price</li>
        <li>/stock/TSLA → Tesla stock price</li>
        <li>/crypto/BTC-USD → Bitcoin price</li>
    </ul>
    """

@app.route('/stock/<symbol>')
def get_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if data.empty:
            return jsonify({"error": "Invalid stock symbol"}), 404
        price = round(data['Close'].iloc[-1], 2)
        return jsonify({"symbol": symbol.upper(), "latest_price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/crypto/<symbol>')
def get_crypto(symbol):
    try:
        crypto = yf.Ticker(symbol)
        data = crypto.history(period="1d")
        if data.empty:
            return jsonify({"error": "Invalid crypto symbol"}), 404
        price = round(data['Close'].iloc[-1], 2)
        return jsonify({"symbol": symbol.upper(), "latest_price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

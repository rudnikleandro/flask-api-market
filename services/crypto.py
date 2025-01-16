import requests
import os

API_KEY = os.getenv("COINMARKETCAP_API_KEY")

def get_crypto_data(symbol):
    """
    Consome a API CoinMarketCap para obter cotações de criptomoedas.
    """
    BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {"symbol": symbol}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "data" in data and symbol in data["data"]:
            crypto_data = data["data"][symbol]
            return {
                "symbol": symbol,
                "name": crypto_data["name"],
                "price_usd": crypto_data["quote"]["USD"]["price"],
                "percent_change_24h": crypto_data["quote"]["USD"]["percent_change_24h"],
            }
        else:
            return {"error": "Criptomoeda não encontrada."}
    except Exception as e:
        return {"error": f"Erro ao buscar dados: {str(e)}"}

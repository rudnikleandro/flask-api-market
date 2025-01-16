import requests
import os

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_data(ticker):
    """
    Consome a API Alpha Vantage para obter cotações de ações.
    """
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "1min",
        "apikey": API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if "Time Series (1min)" in data:
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            last_data = data["Time Series (1min)"][last_refreshed]
            return {
                "ticker": ticker,
                "last_refreshed": last_refreshed,
                "price": last_data["1. open"],
                "volume": last_data["5. volume"],
            }
        else:
            return {"error": "Dados não encontrados para o ticker informado."}
    except Exception as e:
        return {"error": f"Erro ao buscar dados: {str(e)}"}

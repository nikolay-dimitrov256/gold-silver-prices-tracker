import yfinance as yf


def get_global_price(code: str) -> float|None:
    ticker = yf.Ticker(code)

    history = ticker.history(period='1d', interval='1m')
    if history.empty:
        return None

    current_price = history['Close'].iloc[-1]

    return round(current_price, 2)


def get_gold_and_silver_prices() -> dict:
    assets = {
        'gold': 'GC=F',
        'silver': 'SI=F',
    }

    prices = {asset: float(get_global_price(code)) for asset, code in assets.items()}

    return prices

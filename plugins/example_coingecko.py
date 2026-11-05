"""Example plugin: current Bitcoin price from the free CoinGecko API."""

import requests

URL = "https://api.coingecko.com/api/v3/simple/price"


def fetch_data():
    """Every plugin must define fetch_data() and return a dictionary."""
    response = requests.get(
        URL, params={"ids": "bitcoin", "vs_currencies": "usd"}, timeout=10
    )
    response.raise_for_status()
    price = response.json()["bitcoin"]["usd"]
    return {"Coin": "Bitcoin", "Price (USD)": f"${price:,.2f}"}

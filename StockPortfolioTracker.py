
# Task 2: Stock Portfolio Tracker

import csv
from datetime import datetime

stocks = {
    "AAPL": ("Apple", "Technology", 180.00),
    "TSLA": ("Tesla", "Automotive", 250.00),
    "MSFT": ("Microsoft", "Technology", 420.00),
    "GOOGL": ("Alphabet", "Technology", 175.00),
    "AMZN": ("Amazon", "E-Commerce", 190.00),
    "META": ("Meta", "Technology", 500.00),
    "NVDA": ("NVIDIA", "Semiconductors", 135.00),
    "NFLX": ("Netflix", "Entertainment", 650.00)
}


def show_stocks(items=None, title="AVAILABLE STOCKS"):
    items = items or stocks.items()

    print(f"\n{title}")
    print("=" * 68)
    print(f"{'Symbol':<10}{'Company':<18}{'Sector':<22}{'Price':<12}")
    print("-" * 68)

    for symbol, details in items:
        company, sector, price = details
        print(f"{symbol:<10}{company:<18}{sector:<22}${price:.2f}")

    print("=" * 68)
    print("Prices are manually defined sample values.")

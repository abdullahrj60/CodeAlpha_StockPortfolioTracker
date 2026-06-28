
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
def search_stock():
    keyword = input(
        "\nEnter symbol, company, or sector: "
    ).lower().strip()

    if not keyword:
        print("Search value cannot be empty.")
        return

    matches = [
        (symbol, details)
        for symbol, details in stocks.items()
        if keyword in symbol.lower()
        or keyword in details[0].lower()
        or keyword in details[1].lower()
    ]

    if matches:
        show_stocks(matches, "SEARCH RESULTS")
    else:
        print("No matching stock was found.")


def calculate_total(portfolio):
    return sum(
        stocks[symbol][2] * quantity
        for symbol, quantity in portfolio.items()
    )


def get_positive_quantity(message):
    try:
        quantity = int(input(message))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return None

        return quantity

    except ValueError:
        print("Please enter a valid whole number.")
        return None
        
def add_stock(portfolio):
    show_stocks()

    symbol = input(
        "\nEnter stock symbol to add: "
    ).upper().strip()

    if symbol not in stocks:
        print("Invalid stock symbol.")
        return

    quantity = get_positive_quantity(
        "Enter number of shares: "
    )

    if quantity is None:
        return

    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    value = stocks[symbol][2] * quantity

    print(
        f"{quantity} share(s) of {symbol} added."
    )
    print(f"Investment value added: ${value:.2f}")

def remove_stock(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    show_portfolio(portfolio)

    symbol = input(
        "\nEnter stock symbol to remove: "
    ).upper().strip()

    if symbol not in portfolio:
        print("This stock is not in your portfolio.")
        return

    quantity = get_positive_quantity(
        "Enter quantity to remove: "
    )

    if quantity is None:
        return

    if quantity > portfolio[symbol]:
        print(
            "You cannot remove more shares than you own."
        )

    elif quantity == portfolio[symbol]:
        del portfolio[symbol]

        print(
            f"All shares of {symbol} were removed."
        )

    else:
        portfolio[symbol] -= quantity

        print(
            f"{quantity} share(s) of {symbol} removed."
        )
def update_stock(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    show_portfolio(portfolio)

    symbol = input(
        "\nEnter stock symbol to update: "
    ).upper().strip()

    if symbol not in portfolio:
        print("This stock is not in your portfolio.")
        return

    try:
        quantity = int(
            input("Enter new total quantity: ")
        )

        if quantity < 0:
            print("Quantity cannot be negative.")

        elif quantity == 0:
            del portfolio[symbol]

            print(
                f"{symbol} removed from the portfolio."
            )

        else:
            old_quantity = portfolio[symbol]
            portfolio[symbol] = quantity

            print(
                f"{symbol} updated from {old_quantity} "
                f"to {quantity} shares."
            )

    except ValueError:
        print("Please enter a valid whole number.")


def set_budget(current_budget):
    if current_budget:
        print(
            f"\nCurrent budget: ${current_budget:.2f}"
        )
    else:
        print("\nNo budget has been set.")

    try:
        budget = float(
            input(
                "Enter new budget or 0 to remove it: $"
            )
        )

        if budget < 0:
            print("Budget cannot be negative.")
            return current_budget

        if budget == 0:
            print("Budget removed.")
        else:
            print(f"Budget set to ${budget:.2f}.")

        return budget

    except ValueError:
        print("Please enter a valid number.")
        return current_budget

def show_portfolio(portfolio, budget=0):
    print("\nSTOCK PORTFOLIO SUMMARY")
    print("=" * 82)

    if not portfolio:
        print("Your portfolio is currently empty.")
        print("=" * 82)
        return

    total = calculate_total(portfolio)

    print(
        f"{'Symbol':<10}"
        f"{'Company':<18}"
        f"{'Price':<13}"
        f"{'Qty':<8}"
        f"{'Value':<15}"
        f"{'Allocation':<12}"
    )

    print("-" * 82)

    largest_symbol = ""
    largest_value = 0
    total_shares = 0

    for symbol, quantity in portfolio.items():
        company, _, price = stocks[symbol]

        value = price * quantity
        allocation = value / total * 100
        total_shares += quantity

        if value > largest_value:
            largest_symbol = symbol
            largest_value = value

        print(
            f"{symbol:<10}"
            f"{company:<18}"
            f"${price:<12.2f}"
            f"{quantity:<8}"
            f"${value:<14.2f}"
            f"{allocation:.2f}%"
        )

    print("-" * 82)
    print(f"Companies owned: {len(portfolio)}")
    print(f"Total shares: {total_shares}")
    print(f"Total investment value: ${total:.2f}")

    print(
        f"Largest holding: {largest_symbol} "
        f"(${largest_value:.2f})"
    )

    if budget:
        difference = budget - total

        if difference >= 0:
            print(
                f"Remaining budget: ${difference:.2f}"
            )
        else:
            print(
                f"Budget exceeded by: "
                f"${abs(difference):.2f}"
            )

    print("=" * 82)

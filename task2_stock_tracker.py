# ----- Stock Portfolio Tracker -----
# Developed by: <Shreyansh pandey>
# Internship Project: CodeAlpha
# This script calculates the total investment value 
# based on user input and predefined stock prices.

def show_intro():
    print("\n📈 Welcome to My Stock Portfolio Tracker!")
    print("Enter your stock details and see your total investment value.\n")

def get_stock_prices():
    """Predefined stock prices (static data for demo)."""
    return {
        "AAPL": 178.50,
        "TSLA": 255.20,
        "MSFT": 320.10,
        "GOOG": 140.30,
        "AMZN": 130.75
    }

def calculate_investment():
    prices = get_stock_prices()
    portfolio = {}
    total_value = 0.0

    while True:
        stock = input("🔹 Enter stock symbol (or 'done' to finish): ").upper()
        
        if stock == "DONE":
            break

        if stock not in prices:
            print("⚠ Stock not found in the list. Try again.")
            continue

        try:
            qty = int(input(f"🔹 Enter quantity for {stock}: "))
        except ValueError:
            print("⚠ Please enter a valid number.")
            continue

        value = prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + qty
        total_value += value
        print(f"✅ Added {qty} shares of {stock} worth ${value:.2f}")

    # Display summary
    print("\n📊 Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock} - {qty} shares @ ${prices[stock]:.2f} each")

    print(f"\n💰 Total Investment Value: ${total_value:.2f}")

if __name__ == "__main__":
    show_intro()
    calculate_investment()

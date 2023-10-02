class RiskManagement:

    def __init__(self, account_balance, max_risk_per_trade=0.01, max_risk_per_portfolio=0.05, symbols=None):
        self.account_balance = account_balance
        self.max_risk_per_trade = max_risk_per_trade
        self.max_risk_per_portfolio = max_risk_per_portfolio
        self.symbols = symbols or []

    def calculate_position_size(self, entry_price, stop_loss_price):
        """Calculate the position size based on the stop loss and risk per trade."""
        risk_amount = self.account_balance * self.max_risk_per_trade
        risk_per_share = entry_price - stop_loss_price

        # Ensure we don't divide by zero if risk_per_share is zero.
        if risk_per_share == 0:
            return 0

        position_size = risk_amount / risk_per_share
        return position_size

    def check_diversification(self, current_portfolio):
        """Ensure the portfolio isn't overexposed to one asset class."""
        # The logic here is simplistic. In a real-world scenario, you'd check sector exposure, correlations, etc.
        portfolio_value = sum(current_portfolio.values())

        for symbol, value in current_portfolio.items():
            if value / portfolio_value > self.max_risk_per_portfolio:
                return False, f"Overexposed to {symbol}"
        return True, "Portfolio is well diversified"

    def should_take_profit(self, current_price, take_profit_price):
        return current_price >= take_profit_price

    def should_stop_loss(self, current_price, stop_loss_price):
        return current_price <= stop_loss_price


# Example usage:
account_balance = 10000  # Assume an initial balance of $10,000

# Symbols we are interested in
symbols = ["AAPL", "GOOGL", "AMZN", "TSLA", "MSFT"]

# Current portfolio (for diversification check). This represents the current value of each holding.
current_portfolio = {
    "AAPL": 3000,
    "GOOGL": 2000,
    "AMZN": 1500,
    "TSLA": 2000,
    "MSFT": 1500
}

rm = RiskManagement(account_balance, symbols=symbols)

# For a new trade setup:
entry_price = 150  # Example price
stop_loss_price = 140
take_profit_price = 170

position_size = rm.calculate_position_size(entry_price, stop_loss_price)
print(f"Recommended position size: {position_size}")

is_diversified, message = rm.check_diversification(current_portfolio)
print(message)

# Later in the trade...
current_price = 160  # Some new price after entering the trade

if rm.should_take_profit(current_price, take_profit_price):
    print("Take profit now!")
elif rm.should_stop_loss(current_price, stop_loss_price):
    print("Trigger stop loss!")
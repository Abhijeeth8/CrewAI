class Account:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.create_account()
        self.total_deposits = 0

    def create_account(self):
        self.balance = 0.0
        self.holdings = {}
        self.transactions = []

    def deposit_funds(self, amount: float) -> None:
        self.balance += amount
        self.total_deposits += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount
        })

    def withdraw_funds(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({
                "type": "withdrawal",
                "amount": amount
            })
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int, get_share_price: callable) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.balance >= total_cost:
            self.balance -= total_cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append({
                "type": "buy",
                "symbol": symbol,
                "quantity": quantity,
                "price": price
            })
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int, get_share_price: callable) -> bool:
        if symbol in self.holdings and self.holdings[symbol] >= quantity:
            price = get_share_price(symbol)
            total_revenue = price * quantity
            self.balance += total_revenue
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({
                "type": "sell",
                "symbol": symbol,
                "quantity": quantity,
                "price": price
            })
            return True
        return False

    def get_portfolio_value(self, get_share_price: callable) -> float:
        value = self.balance
        for symbol, quantity in self.holdings.items():
            value += get_share_price(symbol) * quantity
        return value

    def calculate_profit_loss(self, get_share_price: callable) -> float:
        current_value = self.get_portfolio_value(get_share_price)
        return current_value - self.total_deposits

    def report_holdings(self) -> dict:
        return self.holdings

    def report_transactions(self) -> list:
        return self.transactions

    def report_profit_loss(self, get_share_price: callable) -> float:
        return self.calculate_profit_loss(get_share_price)


# Example usage of get_share_price
def get_share_price(symbol: str) -> float:
    prices = {
        "AAPL": 150.0,
        "TSLA": 250.0,
        "GOOGL": 2800.0
    }
    return prices.get(symbol, 0.0)
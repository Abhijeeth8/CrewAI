def get_share_price(symbol: str) -> float:
    prices = {
        "AAPL": 150.0,
        "TSLA": 800.0,
        "GOOGL": 2800.0
    }
    return prices.get(symbol, 0.0)

class Account:
    def __init__(self, username: str, initial_deposit: float):
        self.username = username
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        cost = price * quantity
        if self.balance >= cost:
            self.balance -= cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
            self.transactions.append(("buy", symbol, quantity, price))
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if self.holdings.get(symbol, 0) >= quantity:
            price = get_share_price(symbol)
            revenue = price * quantity
            self.balance += revenue
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append(("sell", symbol, quantity, price))
            return True
        return False

    def calculate_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, shares in self.holdings.items():
            total_value += shares * get_share_price(symbol)
        return total_value

    def calculate_profit_loss(self) -> float:
        return self.calculate_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions

# Testing the implementation
account = Account(username="user1", initial_deposit=1000.0)
account.deposit(amount=500.0)
account.buy_shares(symbol="AAPL", quantity=2)
account.sell_shares(symbol="AAPL", quantity=1)
portfolio_value = account.calculate_portfolio_value()
profit_loss = account.calculate_profit_loss()
holdings = account.get_holdings()
transactions = account.get_transactions()

print(portfolio_value, profit_loss, holdings, transactions)
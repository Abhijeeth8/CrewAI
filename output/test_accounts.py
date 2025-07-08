import unittest

# Provided accounts.py code

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

# Unit tests for accounts module

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(username="user1", initial_deposit=1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw_success(self):
        result = self.account.withdraw(500.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 500.0)

    def test_withdraw_fail(self):
        result = self.account.withdraw(1500.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)

    def test_buy_shares_success(self):
        result = self.account.buy_shares("AAPL", 2)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.holdings.get("AAPL"), 2)

    def test_buy_shares_fail(self):
        result = self.account.buy_shares("GOOGL", 1)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)

    def test_sell_shares_success(self):
        self.account.buy_shares("AAPL", 2)
        result = self.account.sell_shares("AAPL", 1)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.holdings.get("AAPL"), 1)

    def test_sell_shares_fail(self):
        result = self.account.sell_shares("AAPL", 1)
        self.assertFalse(result)

    def test_calculate_portfolio_value(self):
        # Initially should be equal to initial deposit
        self.assertEqual(self.account.calculate_portfolio_value(), 1000.0)
        
        # After buying 2 AAPL, the value should reflect the shares
        self.account.buy_shares("AAPL", 2)
        self.assertEqual(self.account.calculate_portfolio_value(), 1000.0)

    def test_calculate_profit_loss(self):
        # Initially should be 0
        self.assertEqual(self.account.calculate_profit_loss(), 0.0)
        
        # After buying 2 AAPL, the P/L should reflect this
        self.account.buy_shares("AAPL", 2)
        self.assertEqual(self.account.calculate_profit_loss(), 0.0)

    def test_get_holdings(self):
        self.account.buy_shares("AAPL", 2)
        self.assertEqual(self.account.get_holdings(), {"AAPL": 2})

    def test_get_transactions(self):
        self.account.deposit(500.0)
        self.account.buy_shares("AAPL", 2)
        self.account.sell_shares("AAPL", 1)
        self.assertEqual(len(self.account.get_transactions()), 3)

class TestGetSharePrice(unittest.TestCase):
    def test_get_share_price_valid(self):
        self.assertEqual(get_share_price("AAPL"), 150.0)
        self.assertEqual(get_share_price("TSLA"), 800.0)
        self.assertEqual(get_share_price("GOOGL"), 2800.0)

    def test_get_share_price_invalid(self):
        self.assertEqual(get_share_price("MSFT"), 0.0)

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import Mock
from accounts import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("user123")
        self.get_share_price_mock = Mock()
        self.get_share_price_mock.side_effect = lambda x: {
            "AAPL": 150.0,
            "TSLA": 250.0,
            "GOOGL": 2800.0
        }.get(x, 0.0)

    def test_initial_account_state(self):
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.total_deposits, 0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit_funds(self):
        self.account.deposit_funds(1000.0)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.total_deposits, 1000.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0]["type"], "deposit")

    def test_withdraw_funds(self):
        self.account.deposit_funds(1000.0)
        result = self.account.withdraw_funds(500.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 500.0)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1]["type"], "withdrawal")

    def test_withdraw_funds_insufficient_balance(self):
        result = self.account.withdraw_funds(500.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 0)

    def test_buy_shares(self):
        self.account.deposit_funds(3000.0)
        result = self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertIn("AAPL", self.account.holdings)
        self.assertEqual(self.account.holdings["AAPL"], 10)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1]["type"], "buy")

    def test_buy_shares_insufficient_funds(self):
        result = self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        self.assertFalse(result)
        self.assertNotIn("AAPL", self.account.holdings)

    def test_sell_shares(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        result = self.account.sell_shares("AAPL", 5, self.get_share_price_mock)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 2250.0)
        self.assertIn("AAPL", self.account.holdings)
        self.assertEqual(self.account.holdings["AAPL"], 5)
        self.assertEqual(len(self.account.transactions), 3)
        self.assertEqual(self.account.transactions[2]["type"], "sell")

    def test_sell_shares_insufficient_shares(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        result = self.account.sell_shares("AAPL", 15, self.get_share_price_mock)
        self.assertFalse(result)
        self.assertEqual(self.account.holdings["AAPL"], 10)

    def test_get_portfolio_value(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        value = self.account.get_portfolio_value(self.get_share_price_mock)
        self.assertEqual(value, 3000.0)

    def test_calculate_profit_loss(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        profit_loss = self.account.calculate_profit_loss(self.get_share_price_mock)
        self.assertEqual(profit_loss, 0.0)
        self.account.sell_shares("AAPL", 10, self.get_share_price_mock)
        profit_loss = self.account.calculate_profit_loss(self.get_share_price_mock)
        self.assertEqual(profit_loss, 1500.0)

    def test_report_holdings(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        holdings = self.account.report_holdings()
        self.assertIn("AAPL", holdings)
        self.assertEqual(holdings["AAPL"], 10)

    def test_report_transactions(self):
        self.account.deposit_funds(3000.0)
        self.assertEqual(len(self.account.report_transactions()), 1)
        self.account.buy_shares("AAPL", 10, self.get_share_price_mock)
        self.assertEqual(len(self.account.report_transactions()), 2)

    def test_report_profit_loss(self):
        self.account.deposit_funds(3000.0)
        profit_loss = self.account.report_profit_loss(self.get_share_price_mock)
        self.assertEqual(profit_loss, 0.0)

if __name__ == "__main__":
    unittest.main()
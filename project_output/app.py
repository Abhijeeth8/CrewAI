import gradio as gr
from accounts import Account, get_share_price

account = Account("user123")

def create_account():
    account.create_account()
    return "Account Created."

def deposit(amount):
    account.deposit_funds(amount)
    return f"Deposited ${amount:.2f}. Current balance: ${account.balance:.2f}."

def withdraw(amount):
    if account.withdraw_funds(amount):
        return f"Withdrew ${amount:.2f}. Current balance: ${account.balance:.2f}."
    else:
        return "Insufficient funds."

def buy_shares(symbol, qty):
    if account.buy_shares(symbol, qty, get_share_price):
        return f"Bought {qty} shares of {symbol}."
    else:
        return "Insufficient balance to buy shares."

def sell_shares(symbol, qty):
    if account.sell_shares(symbol, qty, get_share_price):
        return f"Sold {qty} shares of {symbol}."
    else:
        return "Insufficient shares to sell."

def report_holdings():
    holdings = account.report_holdings()
    return f"Current holdings: {holdings}"

def report_transactions():
    transactions = account.report_transactions()
    return f"Transactions: {transactions}"

def report_profit_loss():
    profit_loss = account.report_profit_loss(get_share_price)
    return f"Profit/Loss: ${profit_loss:.2f}"

# app = gr.Interface(
#     title="Trading Simulation Platform",
#     description="A simple account management for trading.",
#     fn=None,
#     blocks=[],
# )

with gr.Blocks(title="Trading Simulation Platform") as app:
    gr.Markdown("### Account Operations")
    
    create_account_button = gr.Button("Create Account")
    create_acc_sec = gr.Markdown()

    create_account_button.click(create_account, inputs=[], outputs=create_acc_sec)
    
    deposit_amount = gr.Number(label="Deposit Amount")
    deposit_button = gr.Button("Deposit")
    deposit_sec = gr.Markdown()

    deposit_button.click(deposit, inputs=deposit_amount, outputs=deposit_sec)

    withdraw_amount = gr.Number(label="Withdraw Amount")
    withdraw_button = gr.Button("Withdraw")
    withdraw_sec = gr.Markdown()

    withdraw_button.click(withdraw, inputs=withdraw_amount, outputs=withdraw_sec)

    symbol = gr.Textbox(label="Stock Symbol")
    quantity = gr.Number(label="Quantity")
    
    buy_button = gr.Button("Buy Shares")
    buy_sec = gr.Markdown()
    buy_button.click(buy_shares, inputs=[symbol, quantity], outputs=buy_sec)
    
    sell_button = gr.Button("Sell Shares")
    sell_sec = gr.Markdown()
    sell_button.click(sell_shares, inputs=[symbol, quantity], outputs=sell_sec)
    
    holdings_button = gr.Button("View Holdings")
    holdings_sec = gr.Markdown()
    holdings_button.click(report_holdings, inputs=[], outputs=holdings_sec)
    
    transactions_button = gr.Button("View Transactions")
    transactions_sec = gr.Markdown()
    transactions_button.click(report_transactions, inputs=[], outputs=transactions_sec)
    
    profit_loss_button = gr.Button("View Profit/Loss")
    pl_sec = gr.Markdown()
    profit_loss_button.click(report_profit_loss, inputs=[], outputs=pl_sec)

app.launch(share = True)
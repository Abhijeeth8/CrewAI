import gradio as gr
from accounts import Account, get_share_price

# Initialize account
account = Account(username="user1", initial_deposit=1000.0)

def create_account(username, initial_deposit):
    global account
    account = Account(username, initial_deposit)
    return f"Account created for {username} with initial deposit of ${initial_deposit:.2f}"

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited ${amount:.2f}. Current balance: ${account.balance:.2f}"

def withdraw_funds(amount):
    if account.withdraw(amount):
        return f"Withdrew ${amount:.2f}. Current balance: ${account.balance:.2f}"
    else:
        return "Insufficient funds for withdrawal."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, int(quantity)):
        return f"Bought {quantity} shares of {symbol}."
    else:
        return "Insufficient funds to buy shares."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, int(quantity)):
        return f"Sold {quantity} shares of {symbol}."
    else:
        return "Not enough shares to sell."

def report_portfolio_value():
    value = account.calculate_portfolio_value()
    return f"Total Portfolio Value: ${value:.2f}"

def report_profit_loss():
    profit_loss = account.calculate_profit_loss()
    return f"Profit/Loss: ${profit_loss:.2f}"

def report_holdings():
    holdings = account.get_holdings()
    return f"Holdings: {holdings}"

def report_transactions():
    transactions = account.get_transactions()
    return f"Transactions: {transactions}"

# Gradio UI Components
with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Platform")

    with gr.Tab("Account Management"):
        username = gr.Textbox(label="Username")
        initial_deposit = gr.Number(label="Initial Deposit")
        create_button = gr.Button("Create Account")
        create_output = gr.Textbox(label="Create Account Output", interactive=False)

        create_button.click(create_account, inputs=[username, initial_deposit], outputs=create_output)
    
    with gr.Tab("Transactions"):
        amount = gr.Number(label="Amount")
        deposit_button = gr.Button("Deposit")
        withdraw_button = gr.Button("Withdraw")
        trans_output = gr.Textbox(label="Transaction Output", interactive=False)
        
        deposit_button.click(deposit_funds, inputs=amount, outputs=trans_output)
        withdraw_button.click(withdraw_funds, inputs=amount, outputs=trans_output)

        symbol = gr.Dropdown(choices=["AAPL", "TSLA", "GOOGL"], label="Symbol")
        quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy Shares")
        sell_button = gr.Button("Sell Shares")
        shares_output = gr.Textbox(label="Shares Transaction Output", interactive=False)

        buy_button.click(buy_shares, inputs=[symbol, quantity], outputs=shares_output)
        sell_button.click(sell_shares, inputs=[symbol, quantity], outputs=shares_output)

    with gr.Tab("Reports"):
        portfolio_button = gr.Button("Portfolio Value")
        profit_loss_button = gr.Button("Profit/Loss")
        holdings_button = gr.Button("Holdings")
        transactions_button = gr.Button("Transactions")
        report_output = gr.Textbox(label="Report Output", interactive=False)

        portfolio_button.click(report_portfolio_value, outputs=report_output)
        profit_loss_button.click(report_profit_loss, outputs=report_output)
        holdings_button.click(report_holdings, outputs=report_output)
        transactions_button.click(report_transactions, outputs=report_output)

demo.launch()
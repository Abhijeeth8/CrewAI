#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime


from project1.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

os.makedirs('output', exist_ok=True)


# def get_requirements():
#     requirements = """
    # A simple account management system for a trading simulation platform.
    # The system should allow users to create an account, deposit funds, and withdraw funds.
    # The system should allow users to record that they have bought or sold shares, providing a quantity.
    # The system should calculate the total value of the user's portfolio, and the profit or loss from the initial deposit.
    # The system should be able to report the holdings of the user at any point in time.
    # The system should be able to report the profit or loss of the user at any point in time.
    # The system should be able to list the transactions that the user has made over time.
    # The system should prevent the user from withdrawing funds that would leave them with a negative balance, or
    # from buying more shares than they can afford, or selling shares that they don't have.
    # The system has access to a function get_share_price(symbol) which returns the current price of a share, and includes a test implementation that returns fixed prices for AAPL, TSLA, GOOGL.
    # """

#     return requirements

# def get_module_name():
#     module_name = "accounts.py"
#     return module_name

# def get_class_name():
#     class_name = "Account"
#     return class_name


def run(requirements, module_name, class_name):
    """
    Run the research crew.
    """

    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)
    # print(requirements)
    # print(module_name)
    # print(class_name)


# if __name__ == "__main__":
#     run()
"""
This module defines chatbot functions for banking operations.
"""

__author__ = "Anannya"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

ACCOUNTS = {
    123456: {"balance": 1000.0},
    234567: {"balance": 2500.0},
    345678: {"balance": 500.0}
}

VALID_TASKS = ["balance", "deposit"]

def get_task():
    task = input("What task would you like to perform? (balance/deposit): ").strip().lower()
    if task not in VALID_TASKS:
        raise ValueError(f'"{task}" is an unknown task.')
    return task

def get_account_number():
    account_input = input("Enter your 6-digit account number: ")
    if not account_input.isdigit():
        raise TypeError("Account number must be an int type.")
    account_number = int(account_input)
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    return account_number

def get_amount():
    amount_input = input("Enter the amount to deposit: ")
    try:
        amount = float(amount_input)
    except ValueError:
        raise TypeError("Amount must be a numeric type.")
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    return amount

def get_balance(account_number):
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    balance = ACCOUNTS[account_number]["balance"]
    return f"Your current balance for account {account_number} is ${balance:,.2f}."

def make_deposit(account_number, amount):
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a numeric type.")
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    ACCOUNTS[account_number]["balance"] += amount
    return f"You have made a deposit of ${amount:.2f} to account {account_number}."

"""
Author: Anannya Kandhari

This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Anannya"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]
def get_account_number():
    """Prompt user for an account number, validate and return it as int."""
    account_input = input("Please enter your account number: ")
    try:
        account_num = int(account_input)
    except ValueError:
        raise TypeError("Account number must be an int type.")
    if account_num not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    return account_num

def get_amount():
    """Prompt user to input deposit amount and validate it."""
    amount_input = input("Enter an amount: ")
    try:
        amount = float(amount_input)
    except ValueError:
        raise TypeError("Amount must be a numeric type.")
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    return amount

def get_balance(account_number):
    """Return a formatted balance message for the account."""
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    balance = ACCOUNTS[account_number]['balance']
    return f"Your current balance for account {account_number} is ${balance:,.2f}."

def make_deposit(account_number, amount):
    """Deposit amount into the account and return confirmation message."""
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric type.")
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    ACCOUNTS[account_number]['balance'] += amount
    return f"You have made a deposit of ${amount:,.2f} to account {account_number}."

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()

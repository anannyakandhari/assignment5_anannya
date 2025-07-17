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

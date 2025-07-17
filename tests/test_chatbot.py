__author__ = ""
__version__ = "24.3.2025"

import unittest
from unittest.mock import patch
from src.chatbot import (
    get_account_number,
    get_amount,
    get_balance,
    make_deposit,
    get_task,
    ACCOUNTS
)


class TestChatbot(unittest.TestCase):
    """Test class for chatbot module functions."""

    @patch('builtins.input', return_value='non_numeric_data')
    def test_get_account_number_non_numeric_input(self, mock_input):
        with self.assertRaises(TypeError) as context:
            get_account_number()
        
        self.assertEqual(str(context.exception), "Account number must be an int type.")

    # ... (other tests unchanged) ...

    def test_make_deposit_valid_inputs(self):
        account_number = 123456
        amount = 500
        original_balance = ACCOUNTS[account_number]["balance"]  # Access the numeric balance
        expected_message = f"You have made a deposit of ${amount:.2f} to account {account_number}."
        
        result = make_deposit(account_number, amount)
        new_balance = ACCOUNTS[account_number]["balance"]  # Access the updated balance
        
        self.assertEqual(result, expected_message)
        self.assertEqual(new_balance, original_balance + amount)
        
        # Restore original balance so other tests aren't affected
        ACCOUNTS[account_number]["balance"] = original_balance

    # ... (rest of your tests unchanged) ...

if __name__ == "__main__":
    unittest.main()


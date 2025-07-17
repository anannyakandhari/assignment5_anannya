"""
This module defines the TestChatbot class with unit tests for the chatbot functions.
"""

import unittest
from unittest.mock import patch
from src.chatbot import (
    ACCOUNTS, VALID_TASKS, get_task, get_account_number,
    get_amount, get_balance, make_deposit
)

__author__ = "Anannya"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

class TestChatbot(unittest.TestCase):

    # get_task() tests
    @patch('builtins.input', return_value='balance')
    def test_get_task_valid_lowercase(self, mock_input):
        task = get_task()
        self.assertEqual(task, 'balance')

    @patch('builtins.input', return_value='BALANCE')
    def test_get_task_valid_uppercase(self, mock_input):
        task = get_task()
        self.assertEqual(task, 'balance')

    @patch('builtins.input', return_value='Withdraw')
    def test_get_task_invalid(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            get_task()
        self.assertEqual(str(cm.exception), '"withdraw" is an unknown task.')

    # get_account_number() tests
    @patch('builtins.input', return_value='abc')
    def test_get_account_number_not_int(self, mock_input):
        with self.assertRaises(TypeError) as cm:
            get_account_number()
        self.assertEqual(str(cm.exception), "Account number must be an int type.")

    @patch('builtins.input', return_value='999999')
    def test_get_account_number_not_exist(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            get_account_number()
        self.assertEqual(str(cm.exception), "Account number entered does not exist.")

    @patch('builtins.input', return_value='123456')
    def test_get_account_number_valid(self, mock_input):
        account_num = get_account_number()
        self.assertEqual(account_num, 123456)

    # get_amount() tests
    @patch('builtins.input', return_value='abc')
    def test_get_amount_not_numeric(self, mock_input):
        with self.assertRaises(TypeError) as cm:
            get_amount()
        self.assertEqual(str(cm.exception), "Amount must be a numeric type.")

    @patch('builtins.input', return_value='0')
    def test_get_amount_zero(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            get_amount()
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    @patch('builtins.input', return_value='-10')
    def test_get_amount_negative(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            get_amount()
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    @patch('builtins.input', return_value='100.50')
    def test_get_amount_valid(self, mock_input):
        amount = get_amount()
        self.assertEqual(amount, 100.50)

    # get_balance() tests
    def test_get_balance_not_int(self):
        with self.assertRaises(TypeError) as cm:
            get_balance("abc")
        self.assertEqual(str(cm.exception), "Account number must be an int type.")

    def test_get_balance_not_exist(self):
        with self.assertRaises(ValueError) as cm:
            get_balance(999999)
        self.assertEqual(str(cm.exception), "Account number does not exist.")

    def test_get_balance_valid(self):
        account_num = 123456
        expected = f"Your current balance for account {account_num} is ${ACCOUNTS[account_num]['balance']:,.2f}."
        actual = get_balance(account_num)
        self.assertEqual(actual, expected)

    # make_deposit() tests
    def test_make_deposit_account_number_not_int(self):
        with self.assertRaises(TypeError) as cm:
            make_deposit("abc", 100)
        self.assertEqual(str(cm.exception), "Account number must be an int type.")

    def test_make_deposit_account_number_not_exist(self):
        with self.assertRaises(ValueError) as cm:
            make_deposit(999999, 100)
        self.assertEqual(str(cm.exception), "Account number does not exist.")

    def test_make_deposit_non_numeric_amount(self):
        with self.assertRaises(TypeError) as cm:
            make_deposit(123456, "abc")
        self.assertEqual(str(cm.exception), "Amount must be a numeric type.")

    def test_make_deposit_amount_zero(self):
        with self.assertRaises(ValueError) as cm:
            make_deposit(123456, 0)
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    def test_make_deposit_amount_negative(self):
        with self.assertRaises(ValueError) as cm:
            make_deposit(123456, -10)
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    def test_make_deposit_valid_inputs(self):
        account_num = 123456
        amount = 100
        original_balance = ACCOUNTS[account_num]["balance"]
        msg = make_deposit(account_num, amount)
        new_balance = ACCOUNTS[account_num]["balance"]
        self.assertEqual(msg, f"You have made a deposit of ${amount:.2f} to account {account_num}.")
        self.assertEqual(new_balance, original_balance + amount)
        ACCOUNTS[account_num]["balance"] = original_balance  # Reset for other tests

if __name__ == "__main__":
    unittest.main()

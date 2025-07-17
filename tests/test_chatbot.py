"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

vfrom unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS

__author__ = ""
__version__ = ""
__credits__ = "COMP-1327 Faculty"

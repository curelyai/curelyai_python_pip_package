# tests/test_chat.py

import unittest
from curelyai.chat import CurelyAIChat

class TestCurelyAIChat(unittest.TestCase):
    def setUp(self):
        self.chat_client = CurelyAIChat(base_url="http://localhost:8000", bot_key="test_bot_key")
    
    def test_chat(self):
        response = self.chat_client.chat("Hello, how are you?")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()

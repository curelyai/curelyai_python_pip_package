# CurelyAI

Curely AI Official Python SDK

## Installation

```bash
pip install curelyai

from curelyai.chat import CurelyAIChat

# Initialize the chat client with your bot key
chat_client = CurelyAIChat(bot_key="your_bot_key")

# Send a message and print the response
response = chat_client.chat("Hello, how are you?")
print(response)

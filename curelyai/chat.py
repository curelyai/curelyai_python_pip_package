import requests

class CurelyAIChat:
    BASE_URL = "http://localhost:8000"  # API base URL

    def __init__(self, bot_key: str):
        self.bot_key = bot_key
    
    def chat(self, message: str) -> str:
        url = f"{self.BASE_URL}/chat"
        headers = {
            "Content-Type": "application/json",
            "bot_key": self.bot_key
        }
        payload = {
            "message": message
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
        
        return response.json().get("message")

# Usage example (comment this out before publishing)
# if __name__ == "__main__":
#     chat_client = CurelyAIChat(bot_key="your_bot_key")
#     response = chat_client.chat("Hello, how are you?")
#     print(response)

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class AIClient:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY is missing in .env")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
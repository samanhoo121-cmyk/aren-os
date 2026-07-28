from core.ai_client import AIClient

ai = AIClient()

response = ai.generate(
    "Write a short Instagram caption about artificial intelligence"
)

print(response)
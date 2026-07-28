from core.ai_client import AIClient


class AIRouter:

    def __init__(self):
        self.providers = {
            "default": AIClient()
        }

    def generate(self, prompt):
        provider = self.providers["default"]
        return provider.generate(prompt)
from .base_agent import BaseAgent
from core.ai_client import AIClient


class ContentAgent(BaseAgent):

    def __init__(self):
        super().__init__("Content Agent")
        self.ai = AIClient()

    def execute(self, task):
        prompt = f"""
You are a professional content creator.

Create content for this request:

{task}

Return:
1. Hook
2. Main caption
3. Call to action
4. Hashtags
"""

        return self.ai.generate(prompt)
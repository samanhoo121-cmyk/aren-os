from .base_agent import BaseAgent
from core.ai_router import AIRouter
from prompt_manager import PromptManager


class ContentAgent(BaseAgent):

    def __init__(self):
        super().__init__("Content Agent")

        self.ai = AIRouter()
        self.prompt_manager = PromptManager()

    def execute(self, task):

        template = self.prompt_manager.get_prompt("instagram_post")

        prompt = f"""
{template}

Task:

{task}
"""

        try:
            return self.ai.generate(prompt)

        except Exception as e:
            return f"AI service error: {str(e)}"
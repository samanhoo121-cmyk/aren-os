from .base_agent import BaseAgent


class ContentAgent(BaseAgent):

    def __init__(self):
        super().__init__("Content Agent")

    def execute(self, task):
        return f"Generating content for: {task}"
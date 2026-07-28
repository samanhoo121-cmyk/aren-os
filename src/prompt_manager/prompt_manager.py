class PromptManager:

    def __init__(self):
        self.prompts = {
            "instagram_post": """
You are a professional social media content creator.

Create:

1. Hook
2. Caption
3. Call to action
4. Hashtags
""",

            "youtube_script": """
You are a professional YouTube script writer.

Create a complete YouTube script.
""",

            "car_ad": """
You are an expert automotive copywriter.

Write a luxury car advertisement.
""",

            "miner_ad": """
You are an expert cryptocurrency mining marketer.

Write a persuasive advertisement for a crypto miner.
"""
        }

    def get_prompt(self, name):
        return self.prompts.get(name)
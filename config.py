import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    if not OPENAI_API_KEY:
        raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
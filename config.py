import os

class Config:
    """
    Configuration class to hold the OpenAI API key.
    """
    # Retrieve the OpenAI API key from the environment variable
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Raise an error if the OpenAI API key is not set
    if not OPENAI_API_KEY:
        raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
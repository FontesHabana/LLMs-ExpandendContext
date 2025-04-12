import openai
import os
from src.utils import prompts
from src.key import Key

def text_generator(prompt, character, mytemperature=0.5):
    """Generates a list of data based on a prompt and a character."""
    # Sends a request to the API
    response = Key.client.chat.completions.create(
        # Adds a system role to define the character
        messages=[
            {"role": "system", "content": character},  # System message defining the character
            {"role": "user", "content": prompt}        # User message containing the prompt
        ],
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",  # Specifies the model to use
        temperature=mytemperature,  # Controls the randomness of the output
    )
    result = response.choices[0].message.content  # Extracts the content of the first choice
    return result.split("/")  # Returns a list of questions separated by slashes

def expanded_story(prompt, character, mytemperature=0.5):
    """Generates an expanded story."""
    # Sends a request to the API
    response = Key.client.chat.completions.create(
        # Adds a system role to define the character
        messages=[
            {"role": "system", "content": character},  # System message defining the character
            {"role": "user", "content": prompt}        # User message containing the prompt
        ],
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",  # Specifies the model to use
        temperature=mytemperature,  # Controls the randomness of the output
    )
    result = response.choices[0].message.content  # Extracts the content of the first choice
    return result
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

client = genai.Client(api_key=api_key)

def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini API and return the text response.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    return response.text or ""

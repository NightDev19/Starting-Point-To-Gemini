import pytest
from gemini_client import ask_gemini

def test_ask_gemini():
    prompt = "Explain AI in one sentence"
    response = ask_gemini(prompt)

    assert isinstance(response, str), "Response should be a string"
    assert len(response) > 0, "Response should not be empty"
    assert "AI" in response or "ai" in response.lower(), "Response should mention AI"

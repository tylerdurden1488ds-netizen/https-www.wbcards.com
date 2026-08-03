import os

from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_text(prompt: str) -> str:
    """
    Генерация текста через Gemini.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text

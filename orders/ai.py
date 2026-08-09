import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

def ask_gemini(message):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message,
    )
    return response.text
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError ("No API key found")

client = genai.Client(api_key = api_key)
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
model = "gemini-2.5-flash"

generated_content = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
if usage_metadata == None:
    raise RuntimeError ("failed API request")

print(generated_content.text)

def main():
    print("Hello from goldbotai!")


if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError ("No API key found")

    client = genai.Client(api_key = api_key)

    generated_content = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        )
    usage_metadata = generated_content.usage_metadata
    if usage_metadata == None:
        raise RuntimeError ("failed API request")
    print("Prompt tokens:", usage_metadata.prompt_token_count)
    print("Response tokens:", usage_metadata.candidates_token_count)
    print(generated_content.text)


if __name__ == "__main__":
    main(
        
    )

import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError ("No API key found")

    client = genai.Client(api_key = api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    generated_content = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        )
    usage_metadata = generated_content.usage_metadata
    if usage_metadata == None:
        raise RuntimeError ("failed API request")
    if args.verbose == True:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", usage_metadata.prompt_token_count)
        print("Response tokens:", usage_metadata.candidates_token_count)
        print(generated_content.text)
    else:
        print(generated_content.text)


if __name__ == "__main__":
    main(
        
    )

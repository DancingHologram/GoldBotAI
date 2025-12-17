import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


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

    available_functions = types.Tool(
        function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file],
    )

    generated_content = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            )
        )
    usage_metadata = generated_content.usage_metadata
    if usage_metadata == None:
        raise RuntimeError ("failed API request")
    
    if args.verbose == True:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", usage_metadata.prompt_token_count)
        print("Response tokens:", usage_metadata.candidates_token_count)

    if generated_content.function_calls is None:
        print(generated_content.text)
    else:
        for f in generated_content.function_calls:
            print(f"Calling function: {f.name}({f.args})")


if __name__ == "__main__":
    main(
        
    )

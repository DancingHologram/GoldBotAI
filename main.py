import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import call_function, available_functions
import sys


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

    iter_count = 0
    final_response = None

    while iter_count < 20:
        try:
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

            for candidate in generated_content.candidates:
                messages.append(candidate.content)

            if generated_content.function_calls is None:
                final_response = generated_content.text
            else:
                function_responses = []
                for f in generated_content.function_calls:
                    function_call_results = call_function(f, verbose=args.verbose)
                    if not function_call_results.parts or not function_call_results.parts[0].function_response:
                        raise Exception ("empty function call result")
                    if args.verbose:
                        print(f"-> {function_call_results.parts[0].function_response.response}")
                    function_responses.append(function_call_results.parts[0])
                messages.append(types.Content(role="user", parts=function_responses))
            iter_count += 1
            if generated_content.function_calls is None and generated_content.text:
                break
        except Exception as e:
            print(e)
    if iter_count == 20:
        print("Maximum recursion limit reached")
        sys.exit()
    else:
        print(f"Final Response: {final_response}")
        



if __name__ == "__main__":
    main(
        
    )

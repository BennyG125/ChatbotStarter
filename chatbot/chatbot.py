import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the desired GPT model
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    print("Chatbot is ready! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

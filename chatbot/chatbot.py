import openai
from dotenv import load_dotenv
import os
import streamlit as st

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

# Streamlit UI
def main():
    st.title("Chatbot with GPT-3.5 Turbo")
    st.write("Chat with the AI chatbot. Type your message and press 'Send'. Type 'exit' to quit.")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Input box for user message
    user_input = st.text_input("You:", "")

    if user_input:
        # Display user message
        st.session_state['chat_history'].append(f"You: {user_input}")
        
        # Get GPT-3 response
        response = chat_with_gpt(user_input)
        
        # Display bot response
        st.session_state['chat_history'].append(f"Bot: {response}")
    
    # Show chat history in the UI
    for message in st.session_state['chat_history']:
        st.write(message)

    # Clear chat history on 'exit' message
    if 'exit' in user_input.lower():
        st.session_state['chat_history'] = []

if __name__ == "__main__":
    main()

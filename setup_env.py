import os 
from dotenv import load_dotenv

#Loading environment variables from .env
load_dotenv()

#Retrieve the OpenAI key
api_key = os.getenv("OPENAI_API_KEY")

#Print the API key to confirm it is loaded (remember to remove this from production for security)
if api_key:
    print("API key retrieved correctly")
else:
    print("failed to load API key")



from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("OPENAI_API_KEY")
chat = os.getenv("CHATBOT_URL")
database_url = os.getenv("DATABASE_URL")

print(f"API Key: {database_url}")

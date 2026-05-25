import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
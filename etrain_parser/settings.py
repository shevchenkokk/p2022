import os
from dotenv import load_dotenv
load_dotenv()

SECRET_TOKEN = str(os.getenv('SECRET_TOKEN'))
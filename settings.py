import os
from dotenv import load_dotenv

#loading the environment variables
load_dotenv()

global API_URL
API_URL = os.environ["API_URL"]
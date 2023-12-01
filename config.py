import os

from dotenv import load_dotenv

load_dotenv()


# Load the values from the .env file
class Config(object):
    MONGODB_URI = os.environ.get("MONGODB_URI")
    MONGODB_NAME = os.environ.get("MONGODB_NAME")
    PORT = int(os.environ.get("PORT"))

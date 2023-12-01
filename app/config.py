from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    MONGODB_URI = os.environ.get('MONGODB_URI')
    MONGODB_NAME = os.environ.get('MONGODB_NAME')
    PORT = int(os.environ.get('PORT'))


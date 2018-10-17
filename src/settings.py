# settings.py
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


consumer_key=os.environ['TWITTER_API_KEY']
consumer_secret=os.environ['TWITTER_API_SECRET_KEY']

access_token=os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret=os.environ['TWITTER_SECRET_ACCESS_TOKEN']

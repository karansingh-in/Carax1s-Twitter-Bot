import tweepy
import os
import dotenv
dotenv.load_dotenv()

bearer_token = os.getenv('X_BEARER_TOKEN') or os.getenv('bearer_token')
consumer_key = os.getenv('X_API_KEY')
consumer_secret = os.getenv('X_API_SECRET')
access_token = os.getenv('X_ACCESS_TOKEN')
access_token_secret = os.getenv('X_ACCESS_SECRET')


def missing_write_credentials():
    credentials = {
        'X_API_KEY': consumer_key,
        'X_API_SECRET': consumer_secret,
        'X_ACCESS_TOKEN': access_token,
        'X_ACCESS_SECRET': access_token_secret,
    }
    return [name for name, value in credentials.items() if not value]


def create_write_client():
    missing = missing_write_credentials()
    if missing:
        raise RuntimeError(f"Missing X credentials: {', '.join(missing)}")

    return tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )


client = tweepy.Client(bearer_token=bearer_token) if bearer_token else None

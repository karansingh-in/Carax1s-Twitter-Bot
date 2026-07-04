import random

from data import advices, hashtags
from xquik_context import fetch_xquik_context

MAX_TWEET_LENGTH = 280


def trim_tweet(text):
    text = " ".join(text.split())
    if len(text) <= MAX_TWEET_LENGTH:
        return text
    return text[: MAX_TWEET_LENGTH - 3].rstrip() + "..."


def build_advice_tweet(count):
    parts = [
        f"Post {count}",
        random.choice(advices),
        random.choice(hashtags),
    ]
    context = fetch_xquik_context()
    if context:
        parts.append(context)

    return trim_tweet("\n\n".join(parts))

import schedule
import time

from auth import create_write_client
from compose import build_advice_tweet

client = create_write_client()

# POSTING SOMETHING ----
# client.create_tweet(text='this is test 3')

# RETWEETING A POST ----
# client.retweet(1982342611764453882)

# REPLYING TO A POST ----
# client.create_tweet(
#     text="Nice post!",
#     in_reply_to_tweet_id=1982342611764453882
# )

count = int(1)
def job():
    global count
    try:
        client.create_tweet(text=build_advice_tweet(count))
        count += 1
        print("posted something")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    schedule.every().day.at("00:16:00").do(job)
    # schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

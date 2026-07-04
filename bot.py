import random
import schedule
import time
from polls import conduct_polls
from post import post_a_tweet

schedule.every().monday.at(f'07:{random.randint(10, 59)}:17').do(post_a_tweet)
schedule.every().tuesday.at(f'18:{random.randint(10, 59)}:17').do(conduct_polls)

while True:
    schedule.run_pending()
    time.sleep(random.randint(5, 25))

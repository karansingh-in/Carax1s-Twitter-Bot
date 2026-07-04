import random
import schedule
import time
from data import poll_options, poll_questions, hashtags
from auth import create_write_client

client = create_write_client()

def conduct_polls():
    try:
        print('im here')
        number = int(random.randint(1,200))
        client.create_tweet(
        text=poll_questions[number] + '\n\n' + random.choice(hashtags),
        poll_options=poll_options[number],
        poll_duration_minutes=1440
        )  
        print("posted something")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    schedule.every().day.at(f"18:{random.randint(10, 59)}:17").do(conduct_polls)
    while True:
        schedule.run_pending()
        time.sleep(random.randint(5, 25))

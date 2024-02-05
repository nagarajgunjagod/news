# news_scheduler.py

import schedule
import time
import os

def fetch_news():
    os.system("python manage.py fetch_news")

# Schedule the fetch_news function to run every minute
schedule.every(1).minutes.do(fetch_news)

while True:
    schedule.run_pending()
    time.sleep(1)

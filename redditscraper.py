from time import time
import asyncpraw
import os
from dotenv import load_dotenv
load_dotenv()

async def scan_posts():

    reddit = asyncpraw.Reddit(client_id=os.environ.get('CLIENT_ID'),
                              client_secret=os.environ.get('CLIENT_SECRET'),
                              user_agent=os.environ.get('USER_AGENT'))

    subreddit = await reddit.subreddit("linuxmemes")

    url_links = []
    async for submission in subreddit.top(limit=5, time_filter="day"):
          if submission.url.endswith(('jpg', 'png')):
             url_links.append(submission.url)
             url_links.append(submission.title)
             url_links.append(submission.author.name)
             break
    print(url_links)
    return url_links






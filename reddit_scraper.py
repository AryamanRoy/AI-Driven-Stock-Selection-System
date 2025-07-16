import os  # Add this line to import the os module
import praw
import pandas as pd
import time
import random
from dotenv import load_dotenv
from sentiment_analyzer import get_sentiment, classify_sentiment

# Load environment variables
load_dotenv()

# Load API keys from environment variables
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit client
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# Scrape Reddit for posts related to a specific ticker
def scrape_reddit(ticker, subreddits, model, tokenizer, reddit_data, limit=5, interval=30):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    while True:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            posts = []

            for submission in subreddit.new(limit=20):  # Fetch the latest 20 posts
                if ticker.lower() in submission.title.lower():
                    sentiment = get_sentiment(submission.title, model, tokenizer)
                    posts.append({
                        "source": "Reddit",
                        "text": submission.title,
                        "author": submission.author.name if submission.author else "Unknown",
                        "url": submission.url,
                        "sentiment": sentiment,
                        "sentiment_label": classify_sentiment(sentiment)
                    })

            if posts:  # Check if posts is not empty
                # Randomly select 5 posts
                random_posts = random.sample(posts, min(len(posts), limit))  # Ensure len(posts) is an integer
                # Append to CSV
                df = pd.DataFrame(random_posts)
                df.to_csv('continuous_scraper_output_v1.csv', mode='a', header=False, index=False)

                print(f"Scraped and saved {len(random_posts)} Reddit records from {subreddit_name} for {ticker}.")

        time.sleep(interval)

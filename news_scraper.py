import os
import requests
import pandas as pd
import time
import random
import logging
from dotenv import load_dotenv
from sentiment_analyzer import get_sentiment

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

news_api_key = os.getenv("NEWS_API_KEY")


def scrape_news(ticker, limit=5, interval=10):
    while True:
        query = f"{ticker} stock"
        news_data = []

        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={news_api_key}&pageSize=20"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Error fetching news: Status Code {response.status_code}")
                time.sleep(interval)
                continue

            articles = response.json().get('articles', [])
            for article in articles:
                title = article.get('title', 'No Title Found')
                url = article.get('url', 'No URL Found')
                author = article.get('author', 'Unknown')

                sentiment = get_sentiment(title)
                news_data.append({
                    "source": "NewsAPI",
                    "text": title,
                    "author": author,
                    "url": url,
                    "sentiment": sentiment,
                    "sentiment_label": classify_sentiment(sentiment)
                })

            if news_data:
                # Ensure we only sample from the available articles
                num_articles_to_sample = min(len(news_data), limit)
                random_news = random.sample(news_data, num_articles_to_sample)

                # Append to CSV
                df = pd.DataFrame(random_news)
                df.to_csv('continuous_scraper_output_v1.csv', mode='a', header=False, index=False)

                logging.info(f"Scraped and saved {len(random_news)} news articles for {ticker}.")
            else:
                logging.info("No news articles found.")

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
        except Exception as e:
            logging.error(f"Failed to fetch news: {e}")

        # Implement a backoff strategy if rate limit is hit
        time.sleep(interval)


# Example usage
if __name__ == "__main__":
    scrape_news("AMD", limit=5, interval=60)  # Adjust the interval as needed

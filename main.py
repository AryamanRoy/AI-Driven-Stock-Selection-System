import os
import threading
from dotenv import load_dotenv
from reddit_scraper import scrape_reddit
from news_scraper import scrape_news
from sentiment_analyzer import load_sentiment_model
from stock_reccomendation import calculate_average_sentiment, get_recommendation

def main():
    ticker = input("Enter the stock ticker symbol (e.g., AMD): ").strip().upper()
    subreddits = ['stocks', 'wallstreetbets', 'investing', 'finance']
    print(f"Starting continuous web scraping for stock data of {ticker}...")

    # Load sentiment model and tokenizer
    model, tokenizer = load_sentiment_model()

    # Initialize data lists
    news_data = []
    reddit_data = []

    # Create threads for both scraping functions
    reddit_thread = threading.Thread(target=scrape_reddit, args=(ticker, subreddits, model, tokenizer, reddit_data))
    news_thread = threading.Thread(target=scrape_news, args=(ticker, model, tokenizer, news_data))

    # Start both threads
    reddit_thread.start()
    news_thread.start()

    # Wait for both threads to finish
    reddit_thread.join()
    news_thread.join()

    # Calculate average sentiment
    average_sentiment = calculate_average_sentiment(news_data, reddit_data)

    # Get recommendation
    recommendation = get_recommendation(average_sentiment)
    print(f"Recommendation for {ticker}: {recommendation}")


if __name__ == "__main__":
    main()

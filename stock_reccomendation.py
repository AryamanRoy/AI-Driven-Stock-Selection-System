import yfinance as yf

def get_historical_data(ticker):
    stock_data = yf.download(ticker, period="1y")  # Fetch 1 year of historical data
    return stock_data

def get_recommendation(average_sentiment):
    # Define thresholds
    buy_threshold = 0.7  # Example threshold for BUY
    sell_threshold = 0.3  # Example threshold for SELL

    if average_sentiment >= buy_threshold:
        return "BUY"
    elif average_sentiment <= sell_threshold:
        return "SELL"
    else:
        return "HOLD"


def calculate_average_sentiment(news_data, reddit_data):
    total_sentiment = 0
    total_count = 0

    # Calculate sentiment from news data
    for news in news_data:
        total_sentiment += news['sentiment']
        total_count += 1

    # Calculate sentiment from Reddit data
    for reddit in reddit_data:
        total_sentiment += reddit['sentiment']
        total_count += 1

    if total_count == 0:
        return 0  # Avoid division by zero

    return total_sentiment / total_count


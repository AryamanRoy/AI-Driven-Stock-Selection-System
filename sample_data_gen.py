import pandas as pd
import random

# Sample data generation
data = {
    "text": [],
    "sentiment": [],
    "source": []
}

# Sample phrases for different sentiments
phrases = {
    0: ["The company's future looks bleak.", "Investors are worried about the upcoming earnings report.",
        "The stock is plummeting due to poor performance."],
    1: ["The stock has been underperforming lately.", "There are concerns about the company's management.",
        "Market analysts are cautious about this stock."],
    2: ["The stock is stable but not showing much growth.", "Investors are waiting for more information.",
        "The market is uncertain about this company's future."],
    3: ["The company is expected to perform well in the next quarter.",
        "Investors are optimistic about the new product launch.", "The stock is gaining traction in the market."],
    4: ["The company's recent innovations are impressive.", "Investors are excited about the upcoming earnings report.",
        "The stock is soaring due to strong demand."]
}

# Generate 1500 entries
for _ in range(15000):
    sentiment = random.choice(list(phrases.keys()))
    text = random.choice(phrases[sentiment])
    source = random.choice(["NewsAPI", "Reddit"])

    data["text"].append(text)
    data["sentiment"].append(sentiment)
    data["source"].append(source)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('financial_sentiment_data.csv', index=False)

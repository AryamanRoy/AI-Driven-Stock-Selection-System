import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the sentiment model and tokenizer
def load_sentiment_model():
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"  # Pre-trained model for sentiment analysis
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return model, tokenizer

# Function to predict sentiment
def predict_sentiment(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    return predicted_class  # 0: Negative, 1: Positive

# Function to classify sentiment
def classify_sentiment(predicted_class):
    if predicted_class == 0:
        return "Negative"
    elif predicted_class == 1:
        return "Positive"

# Function to get sentiment
def get_sentiment(text, model, tokenizer):
    predicted_class = predict_sentiment(text, model, tokenizer)
    return predicted_class

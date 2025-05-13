import requests

def get_user(user_id):
    url = f"https://api.example.com/users/{user_id}"
    return requests.get(url)

# --- Example: utils/ai_utils.py ---
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_chatbot_response(text):
    result = sentiment_model(text)
    return result[0]['label']
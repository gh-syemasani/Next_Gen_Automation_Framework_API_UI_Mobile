# --- Example: utils/ai_utils.py ---
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import openai
import os

# Sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# Embedding model for similarity
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Configure OpenAI API key if needed
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_sentiment(text):
    """Returns the sentiment label of the given text."""
    result = sentiment_model(text)
    return result[0]['label'], result[0]['score']

def compute_similarity(text1, text2):
    """Returns cosine similarity score between two texts."""
    embedding1 = embedding_model.encode(text1, convert_to_tensor=True)
    embedding2 = embedding_model.encode(text2, convert_to_tensor=True)
    return float(util.pytorch_cos_sim(embedding1, embedding2).item())

def ask_llm(prompt, model="gpt-3.5-turbo"):
    """Asks a question to an OpenAI LLM and returns the response."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"LLM error: {str(e)}"

# Example utilities that can be used in chatbot testing

def verify_chatbot_response_quality(response_text):
    sentiment, confidence = analyze_sentiment(response_text)
    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "is_positive": sentiment == "POSITIVE"
    }

def compare_expected_vs_actual(expected, actual):
    score = compute_similarity(expected, actual)
    return score >= 0.8  # Threshold for acceptance
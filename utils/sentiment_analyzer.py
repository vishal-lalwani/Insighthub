# utils/sentiment_analyzer.py
from textblob import TextBlob

def analyze_sentiment(text: str):
    """
    Returns (label, score) where score is polarity in [-1, 1]
    and label is one of 'Positive', 'Neutral', 'Negative'.
    """
    if not text:
        return "Neutral", 0.0

    analysis = TextBlob(text)
    score = round(analysis.sentiment.polarity, 4)

    if score > 0.2:
        label = "Positive"
    elif score < -0.2:
        label = "Negative"
    else:
        label = "Neutral"

    return label, float(score)

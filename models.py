from textblob import TextBlob

def analyze_email(text):
    # Sentiment Analysis
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Priority
    urgent_keywords = ["urgent", "immediately", "critical", "cannot access"]
    priority = "Urgent" if any(word in text.lower() for word in urgent_keywords) else "Not Urgent"

    return sentiment, priority


def generate_response(text, sentiment, priority):
    # Simple rule-based reply
    if priority == "Urgent":
        reply = "We acknowledge your urgent issue. Our support team is working on it immediately."
    else:
        reply = "Thank you for reaching out. We will look into your request and get back to you soon."

    if sentiment == "Negative":
        reply = "We understand your frustration. " + reply
    elif sentiment == "Positive":
        reply = "We appreciate your feedback. " + reply

    return reply

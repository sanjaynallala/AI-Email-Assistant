from textblob import TextBlob
from utils import extract_contact_info, extract_products_or_keywords

def analyze_email(text):
    # sentiment
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    # priority (binary)
    urgent_keywords = ["urgent","immediately","critical","cannot access","asap","down"]
    is_urgent = any(k in text.lower() for k in urgent_keywords)
    priority = "Urgent" if is_urgent else "Not Urgent"
    # score for queueing
    score = (1 if is_urgent else 0) * 10 + (abs(polarity) * 3)
    return sentiment, priority, score

# Rule-based reply generator (good fallback)
def generate_rule_response(text, sentiment, priority):
    products = extract_products_or_keywords(text)
    prod_str = f" regarding {', '.join(products)}" if products else ""
    if priority == "Urgent":
        reply = "We acknowledge your urgent issue" + prod_str + ". Our support team is investigating this immediately and will update you shortly."
    else:
        reply = "Thank you for reaching out" + prod_str + ". We will review your request and get back within 24 hours."
    if sentiment == "Negative":
        reply = "We are sorry to hear about your experience. " + reply
    elif sentiment == "Positive":
        reply = "Thanks for the feedback! " + reply
    return reply

# LLM prompt template (use if you integrate OpenAI/HuggingFace)
LLM_PROMPT = """
You are a professional, empathetic customer support assistant.
Email: {email_body}
Sentiment: {sentiment}
Priority: {priority}
Products: {products}
Write a concise (2-5 sentence), professional reply that:
- Acknowledges the customer's issue and sentiment
- Offers next steps and an ETA where possible
- References the product if present
Reply:
"""
def llm_prompt_for_email(body, sentiment, priority, products):
    return LLM_PROMPT.format(email_body=body, sentiment=sentiment, priority=priority, products=", ".join(products))

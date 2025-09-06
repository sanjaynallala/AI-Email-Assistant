import re

def extract_info(text):
    email_match = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    phone_match = re.findall(r"\+?\d[\d -]{8,12}\d", text)
    return {"emails": email_match, "phones": phone_match}

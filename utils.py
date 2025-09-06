import re

def extract_contact_info(text):
    emails = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    phones = re.findall(r"\+?\d[\d \-\(\)]{7,}\d", text)
    return {"emails": list(set(emails)), "phones": list(set(phones))}

def extract_products_or_keywords(text, product_list=None):
    if product_list is None:
        product_list = ["product", "dashboard", "login", "subscription", "account"]
    found = [p for p in product_list if p in text.lower()]
    return found

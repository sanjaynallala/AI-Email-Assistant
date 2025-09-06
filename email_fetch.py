import pandas as pd
from datetime import datetime, timedelta

def load_emails(csv_path="Sample_Support_Emails_Dataset.csv"):
    df = pd.read_csv(csv_path)
    # normalize column names
    df.columns = [c.strip().lower() for c in df.columns]
    # ensure sent_date is datetime if possible (if ####### placeholder, skip)
    try:
        df['sent_date'] = pd.to_datetime(df['sent_date'])
    except:
        # if corrupted timestamps, create synthetic recent times
        now = datetime.utcnow()
        df['sent_date'] = [now - timedelta(hours=i) for i in range(len(df))]
    return df

# Filter by subject keywords
def filter_support_emails(df, keywords=None):
    if keywords is None:
        keywords = ["support", "query", "request", "help"]
    mask = df['subject'].str.contains("|".join(keywords), case=False, na=False)
    return df[mask].reset_index(drop=True)

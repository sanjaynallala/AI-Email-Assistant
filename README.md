## Requirements Coverage

This submission implements the required features:

- Email Retrieval & Filtering
  - Simulated retrieval from provided CSV (`email_fetch.py`)
  - Filters by subject keywords: "support","query","request","help"

- Extracted details shown on dashboard:
  - Sender's email
  - Subject
  - Body (preview)
  - Date/time received

- Categorization & Prioritization
  - Sentiment analysis (TextBlob) => Positive/Neutral/Negative
  - Priority detection (keyword-based); Urgent emails flagged
  - Priority queue ordering implemented (`priority_queue.py`)

- Context-Aware Auto-Responses
  - Rule-based response generator using sentiment + priority
  - LLM prompt template included for optional OpenAI/HuggingFace integration (do not include API keys in repo)

- Information Extraction
  - Contact details (emails, phones) extracted using regex (`utils.py`)
  - Product / keyword extraction for contextual replies

- Dashboard / UI (Streamlit)
  - Filtered email list + extracted key details
  - Analytics: sentiment distribution, priority counts, emails last 24h, resolved & pending
  - AI-generated responses editable in UI

- Deliverables included:
  - Working Streamlit app (app.py)
  - Code for sentiment/priority/extraction/response
  - README and demo script

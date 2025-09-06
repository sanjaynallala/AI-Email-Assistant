import streamlit as st
import pandas as pd
import plotly.express as px
from models import analyze_email, generate_response
from utils import extract_info

# Load dataset
df = pd.read_csv("Sample_Support_Emails_Dataset.csv")

st.set_page_config(page_title="AI Email Assistant", layout="wide")
st.title("📧 AI-Powered Communication Assistant")
st.write("Filter, analyze, and auto-respond to customer support emails")

# Keywords for filtering
keywords = ["support", "query", "request", "help"]
df_filtered = df[df["subject"].str.contains("|".join(keywords), case=False, na=False)]

# Analyze emails
analysis = []
for _, row in df_filtered.iterrows():
    sentiment, priority = analyze_email(str(row["body"]))
    response = generate_response(str(row["body"]), sentiment, priority)
    info = extract_info(str(row["body"]))
    analysis.append({
        "Sender": row["sender"],
        "Subject": row["subject"],
        "Body": row["body"][:80] + "...",  # shorten for display
        "Date": row["sent_date"],
        "Sentiment": sentiment,
        "Priority": priority,
        "Extracted Info": info,
        "Response": response
    })

result_df = pd.DataFrame(analysis)

# Display table
st.subheader("📋 Filtered & Analyzed Emails")
st.dataframe(result_df[["Sender", "Subject", "Sentiment", "Priority"]])

# Charts
col1, col2 = st.columns(2)
with col1:
    fig_sentiment = px.pie(result_df, names="Sentiment", title="Sentiment Distribution")
    st.plotly_chart(fig_sentiment, use_container_width=True)
with col2:
    fig_priority = px.bar(result_df, x="Priority", title="Priority Counts")
    st.plotly_chart(fig_priority, use_container_width=True)

# Responses
st.subheader("🤖 AI Draft Responses")
for i, row in result_df.iterrows():
    st.write(f"**From:** {row['Sender']} | **Subject:** {row['Subject']}")
    st.text_area("Draft Reply", row["Response"], key=f"resp_{i}")

import streamlit as st
from datetime import datetime, timedelta
# assume result_df exists and has Date column parsed as datetime and a 'Priority' column

# Convert Date column to datetime if not already
result_df['Date'] = pd.to_datetime(result_df['Date'], errors='coerce')

# Simple resolved/pending toggles (in this demo it's manual toggling)
st.subheader("Status")
# initialize session state for statuses
if 'statuses' not in st.session_state:
    st.session_state['statuses'] = {i: "Pending" for i in result_df.index}

for i, row in result_df.iterrows():
    cols = st.columns([3,1,1])
    cols[0].write(f"**{row['Subject']}** from {row['Sender']}")
    cols[1].write(st.session_state['statuses'].get(i))
    if cols[2].button("Mark Resolved", key=f"res_{i}"):
        st.session_state['statuses'][i] = "Resolved"

# Metrics: last 24 hours, counts
last_24 = datetime.utcnow() - timedelta(hours=24)
recent_count = result_df[result_df['Date'] >= last_24].shape[0]
resolved_count = sum(1 for v in st.session_state['statuses'].values() if v=="Resolved")
pending_count = sum(1 for v in st.session_state['statuses'].values() if v=="Pending")

st.metric("Emails last 24h", recent_count)
st.metric("Resolved", resolved_count)
st.metric("Pending", pending_count)

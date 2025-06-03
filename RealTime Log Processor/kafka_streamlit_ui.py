import streamlit as st
from kafka import KafkaConsumer

import re
import time

st.set_page_config(page_title="Kafka Log Stream", layout="wide")
st.title("📡 Real-time Kafka Log Stream with Filters")

# Controls
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    log_level = st.selectbox("Filter by Log Level", ["ALL", "INFO", "WARNING", "ERROR", "CRITICAL"])

with col2:
    pause = st.checkbox("Pause Streaming", value=False)

with col3:
    search_term = st.text_input("Search Keyword")

download = st.button("Download Logs")
log_area = st.empty()

@st.cache_resource(show_spinner=False)
def get_consumer():
    return KafkaConsumer(
        'app-logs',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='streamlit-log-viewer',
        value_deserializer=lambda x: x.decode('utf-8'),
        consumer_timeout_ms=1000
    )

consumer = get_consumer()

if "log_buffer" not in st.session_state:
    st.session_state.log_buffer = []

def filter_logs(logs, level_filter, keyword):
    filtered = []
    level_regex = re.compile(r"\b(INFO|WARNING|ERROR|CRITICAL)\b", re.IGNORECASE)
    for log in logs:
        match = level_regex.search(log)
        found_level = match.group(1).upper() if match else "INFO"
        if level_filter != "ALL" and found_level != level_filter:
            continue
        if keyword and keyword.lower() not in log.lower():
            continue
        filtered.append(log)
    return filtered

def colorize(log):
    if "ERROR" in log.upper():
        return f"<span style='color:red'>{log}</span>"
    elif "WARNING" in log.upper():
        return f"<span style='color:orange'>{log}</span>"
    elif "CRITICAL" in log.upper():
        return f"<span style='color:darkred; font-weight:bold'>{log}</span>"
    elif "INFO" in log.upper():
        return f"<span style='color:green'>{log}</span>"
    return log

# Main loop
while True:
    if not pause:
        try:
            msgs = consumer.poll(timeout_ms=500)
            for _, messages in msgs.items():
                for msg in messages:
                    st.session_state.log_buffer.append(msg.value)
            st.session_state.log_buffer = st.session_state.log_buffer[-500:]
        except Exception as e:
            st.error(f"Kafka error: {e}")

    filtered = filter_logs(st.session_state.log_buffer, log_level, search_term)
    display_logs = [colorize(line) for line in reversed(filtered)]

    log_area.markdown(
        "<br>".join(display_logs),
        unsafe_allow_html=True
    )

    if download:
        st.download_button(
        label="Click to download logs",
        data="\n".join(filtered),
        file_name="kafka_logs.txt",
        key="download_button_logs"
        )



    time.sleep(1)

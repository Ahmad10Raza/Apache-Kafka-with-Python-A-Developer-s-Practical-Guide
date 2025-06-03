import streamlit as st
from kafka import KafkaConsumer
import notify2
# import smtplib
# from email.message import EmailMessage

# Initialize desktop notifier
notify2.init("Kafka Log Alert")

# Streamlit UI setup
st.set_page_config(page_title="Real-Time Kafka Log Viewer", layout="wide")
st.title("📊 Real-Time Kafka Log Processor UI")

topic = st.text_input("Enter Kafka Topic", value="logs")
bootstrap_servers = st.text_input("Bootstrap Servers", value="localhost:9092")
search_keyword = st.text_input("Search logs for keyword", value="")
download = st.checkbox("Enable download of filtered logs")

# Connect to Kafka
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='log-ui-group'
)

# Function to send desktop notification
def desktop_notify(msg):
    n = notify2.Notification("🚨 Critical Log Detected", msg)
    n.set_urgency(notify2.URGENCY_CRITICAL)
    n.show()

# Optional: Send email notification
# def send_email_alert(subject, content):
#     msg = EmailMessage()
#     msg.set_content(content)
#     msg['Subject'] = subject
#     msg['From'] = "your_email@gmail.com"
#     msg['To'] = "receiver_email@gmail.com"
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login("your_email@gmail.com", "your_app_password")
#         smtp.send_message(msg)

st.subheader("📜 Log Output")
log_box = st.empty()
filtered = []

# Stream Kafka messages
for msg in consumer:
    log_line = msg.value.decode("utf-8")

    if search_keyword.lower() in log_line.lower():
        filtered.append(log_line)

    # Display log
    log_box.text_area("Real-Time Logs", value="\n".join(filtered[-100:]), height=400)

    # Trigger alert
    if "ERROR" in log_line or "CRITICAL" in log_line:
        st.error(f"🚨 Alert: {log_line}")
        desktop_notify(log_line)
        # send_email_alert("Kafka Critical/Error Log", log_line)

    # Allow download
    if download:
        st.download_button(
            label="Click to download logs",
            data="\n".join(filtered),
            file_name="kafka_logs.txt",
            key="download_button_logs"
        )

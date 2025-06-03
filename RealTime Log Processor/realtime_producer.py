from kafka import KafkaProducer
import time
import os

# Path to system log file (Ubuntu default)
LOG_FILE = "/var/log/syslog"

# Set up Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')
)

def follow(file):
    file.seek(0, os.SEEK_END)  # Go to end of file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line.strip()

try:
    with open(LOG_FILE, 'r') as logfile:
        print(f"📡 Streaming logs from: {LOG_FILE}")
        for log_line in follow(logfile):
            producer.send("app-logs", value=log_line)
            print(f"➡️ Sent: {log_line}")
except KeyboardInterrupt:
    print("\n❌ Stopped by user")
finally:
    producer.flush()
    producer.close()

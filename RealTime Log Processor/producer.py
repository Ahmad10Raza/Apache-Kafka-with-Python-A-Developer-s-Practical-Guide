from kafka import KafkaProducer
import time

# Connect to Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the log file
with open("sample.log", "r") as file:
    for line in file:
        # Send each line as UTF-8 encoded message
        producer.send("app-logs", value=line.strip().encode('utf-8'))
        print(f"Sent: {line.strip()}")
        time.sleep(1)  # simulate real-time delay

# Flush and close the producer
producer.flush()
producer.close()

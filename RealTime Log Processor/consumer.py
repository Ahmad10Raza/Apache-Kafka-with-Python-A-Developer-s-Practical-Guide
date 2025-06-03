from kafka import KafkaConsumer

# Connect to Kafka and subscribe to the topic
consumer = KafkaConsumer(
    'app-logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # start from beginning
    enable_auto_commit=True,
    group_id='log-consumers',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Listening for log messages...\n")

# Consume messages and filter
for message in consumer:
    log = message.value
    if "ERROR" in log or "WARNING" in log:
        print(f"⚠️  Important Log: {log}")
    else:
        print(f"ℹ️  Info: {log}")

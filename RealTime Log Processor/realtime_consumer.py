from kafka import KafkaConsumer

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'app-logs',  # Topic name
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',  # Start from latest message
    enable_auto_commit=True,
    group_id='realtime-log-consumer',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("\n📥 Listening for real-time logs from Kafka...\n")

try:
    for message in consumer:
        log = message.value
        if any(level in log for level in ["ERROR", "WARNING", "CRITICAL"]):
            print(f"⚠️  Important Log: {log}")
        else:
            print(f"ℹ️  Log: {log}")
except KeyboardInterrupt:
    print("\n❌ Consumer stopped by user.")
finally:
    consumer.close()

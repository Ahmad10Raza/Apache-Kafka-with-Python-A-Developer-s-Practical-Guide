from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'temperature-readings',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # read from beginning
    enable_auto_commit=True,
    group_id='temp-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🚀 Listening for temperature data...\n")

# Read and print messages
for message in consumer:
    data = message.value
    print(f"🌡️ Sensor: {data['sensor_id']}, Temp: {data['temperature']}°C, Time: {data['timestamp']}")

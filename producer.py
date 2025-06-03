from kafka import KafkaProducer
import json
from datetime import datetime
import random
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send 10 temperature readings
for i in range(10):
    data = {
        "sensor_id": f"sensor_{random.randint(1, 3)}",
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "timestamp": datetime.now().isoformat()
    }

    producer.send('temperature-readings', value=data)
    print(f"✅ Sent: {data}")
    time.sleep(1)

# Close producer
producer.flush()
producer.close()


## 📌 **Project Title: Real-Time Log Processor using Apache Kafka and Python**

---

## 🎯 **Goal:**

Capture logs from applications in real time, stream them to Kafka topics, and process/display them using Python consumers.

---

## 🗺️ **Roadmap**

---

### 🔹 Phase 1: Environment Setup

1. ✅ **Install Java (JDK)**
2. ✅ **Install and Setup Apache Kafka & Zookeeper**
   * Write a shell script to start both
3. ✅ **Install Python Kafka Client**
   ```bash
   pip install kafka-python
   ```
4. ✅ **Verify Kafka CLI commands**
   * Create topic
   * Produce test message
   * Consume via terminal

---

### 🔹 Phase 2: Design Architecture

* 🧭 Components:
  1. Log Producer (Python): Reads logs and pushes to Kafka
  2. Kafka Broker: Routes messages to topic
  3. Log Consumer (Python): Consumes and processes logs
* 🗂 Topics:
  * `app-logs`
* 🧱 Real-life example:
  * `Producer` → tailing `/var/log/syslog`
  * `Consumer` → storing filtered error logs to `error_logs.txt`

---

### 🔹 Phase 3: Build the Producer (Log Generator)

* Reads from a simulated or real log file
* Sends log lines to Kafka topic (`app-logs`)

```python
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

log_file = open('sample.log')

for line in log_file:
    producer.send('app-logs', value=line.encode('utf-8'))
    time.sleep(1)
```

---

### 🔹 Phase 4: Build the Consumer (Log Processor)

* Reads messages from `app-logs`
* Filters for lines with `ERROR`, `WARNING`, etc.
* Writes to a new file `error_logs.txt`

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'app-logs',
    bootstrap_servers='localhost:9092',
    group_id='log-processors',
    auto_offset_reset='earliest'
)

with open("error_logs.txt", "a") as f:
    for msg in consumer:
        line = msg.value.decode('utf-8')
        if "ERROR" in line or "WARNING" in line:
            f.write(line)
```

---

### 🔹 Phase 5: Add JSON + Serialization (Optional)

* Format logs in JSON:

  `{"timestamp": "2025-06-02T13:05:34", "level": "ERROR", "message": "Something failed"}`
* Use JSON serializer/deserializer in Python

---

### 🔹 Phase 6: Enhance with Features

1. Add multiple consumers:
   * One for saving errors
   * One for real-time dashboard (print on terminal)
2. Add **manual commit** logic for reliability
3. Add **partitioning by log level** using producer keys

---

### 🔹 Phase 7: Testing & Monitoring

* Simulate logs with different levels
* Crash producer and consumer to test offset recovery
* Add logging & retry mechanisms

---

### 🔹 Phase 8: Packaging & Deployment

* Use `docker-compose` for Kafka, Zookeeper, producer, consumer
* Create README for setup
* Create GitHub repo and share logs via live terminal dashboard or file

---

## 🧠 Optional Add-ons

* Use **Flask** or **FastAPI** to expose logs via API
* Use **Kafka Connect + Elasticsearch** to index logs
* Use **Grafana + Prometheus** to monitor processing rate


## ✅ Phase 2: Design Architecture

### 🎯 Goal

Design how data flows between the producer, Kafka, and consumers to simulate and process real-time logs.

---

### 🧱 System Components

| Component              | Description                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **Log Producer** | Python script that reads logs (e.g., simulated or from `/var/log/syslog`) and pushes them to Kafka |
| **Kafka Broker** | Receives and stores messages in a topic                                                              |
| **Log Consumer** | Python script that reads from the topic and processes logs (e.g., filters errors)                    |

---

### 🧵 Kafka Topic Design

* **Topic Name:** `app-logs`
* **Partitions:** At least 1 (or more if you want parallel consumers)
* **Key (Optional):** Use log level (`ERROR`, `INFO`) as key if needed

---

### 🔁 Data Flow

```
[ log file ] → [ Producer.py ] → [ Kafka Topic: app-logs ] → [ Consumer.py ]
                                                   ↓
                                                 [ Consumer #2 (optional): Dashboard / JSON Parser ]
```

---

### 💡 Real-world Mapping

| Component   | Example in real world                        |
| ----------- | -------------------------------------------- |
| Producer    | A microservice generating logs (e.g., Nginx) |
| Kafka Topic | Log router/middleman                         |
| Consumer    | ELK Stack, Datadog, or in-house alert system |

---

### 🧪 Logs to Simulate (Examples)

```text
[2025-06-02 17:10:01] INFO Server started on port 8080
[2025-06-02 17:10:05] WARNING Memory usage is high
[2025-06-02 17:10:10] ERROR Failed to connect to database
```

---



Perfect! Let’s proceed step by step.

---

## 🔧 Step 1: Create Kafka Topic (`app-logs`)

### ✅ Run this in your terminal:

```bash
kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --replication-factor 1 \
  --partitions 1 \
  --topic app-logs
```

To verify the topic was created:

```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

---

## 📄 Step 2: Create a Sample Log File

### ✅ Run this in your project directory:

```bash
cat <<EOF > sample.log
[2025-06-02 17:10:01] INFO Server started on port 8080
[2025-06-02 17:10:05] WARNING Memory usage is high
[2025-06-02 17:10:10] ERROR Failed to connect to database
[2025-06-02 17:10:15] INFO Request processed in 120ms
[2025-06-02 17:10:20] ERROR Timeout connecting to Redis
[2025-06-02 17:10:25] INFO Health check passed
EOF
```

It creates a file `sample.log` that will be streamed by the producer.

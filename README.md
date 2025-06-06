

# Apache Kafka with Python – A Developer's Practical Guide 🚀

Welcome to your end-to-end Kafka learning journey! This project-based repository is built to help you learn and implement Apache Kafka from **scratch to production** using **Python**, **Streamlit**, **Docker**, and **cloud services** like **Confluent Cloud** and **AWS MSK**.

---

## 📚 Table of Contents

- [🔍 Overview](#-overview)
- [📦 Kafka Core Concepts](#-kafka-core-concepts)
- [💻 Local Kafka Setup (Ubuntu)](#-local-kafka-setup-ubuntu)
- [⚙️ CLI Commands](#️-cli-commands)
- [🐍 Kafka with Python](#-kafka-with-python)
- [📈 Real-Time Log Processor Project](#-real-time-log-processor-project)
- [📊 Streamlit UI for Logs](#-streamlit-ui-for-logs)
- [📢 Notification for Critical Logs](#-notification-for-critical-logs)
- [🐳 Kafka with Docker Compose](#-kafka-with-docker-compose)
- [☁️ Kafka on Confluent Cloud / AWS MSK](#️-kafka-on-confluent-cloud--aws-msk)
- [🧠 Advanced Kafka](#-advanced-kafka)
- [🔚 Conclusion](#-conclusion)

---

## 🔍 Overview

This repository guides you through:

- Kafka fundamentals
- Building producers and consumers in Python
- Real-time data processing
- Log visualization with UI
- Deployment via Docker & Cloud

---

## 📦 Kafka Core Concepts

- **Topics, Partitions, Offsets**
- **Producers / Consumers**
- **Consumer Groups**
- **Broker & Zookeeper**
- **Serialization / Deserialization**
- **Commit Mechanism: Auto vs Manual**
- **Sync vs Async Producers**

---

## 💻 Local Kafka Setup (Ubuntu)

> 🧰 All instructions and shell scripts are provided.

- Install Kafka & Zookeeper manually
- Start both with shell scripts
- Kafka CLI: Create topic, produce/consume messages
- Handle connection errors and permissions

---

## ⚙️ CLI Commands

```bash
# Create Topic
kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test-topic --partitions 1 --replication-factor 1

# Produce Message
kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic

# Consume Message
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```


---

## 🐍 Kafka with Python

* Install Python Kafka client:
  ```bash
  pip install kafka-python
  ```
* Build:
  * `producer.py` — sends messages to Kafka
  * `consumer.py` — consumes messages from Kafka
* Implement JSON serialization & deserialization
* Real-time producer that reads system logs

---

## 📈 Real-Time Log Processor Project

✅ A complete Kafka-based pipeline to stream logs in real-time.

### Features:

* Real-time log ingestion from `/var/log`
* Kafka producer continuously streams logs
* Kafka consumer processes logs
* Filters and downloads error/critical logs

---

## 📊 Streamlit UI for Logs

* View logs in real-time on web UI
* Filter by keywords (e.g., "error", "critical")
* Download filtered logs
* Auto refresh log panel

---

## 📢 Notification for Critical Logs

* Sends desktop notifications when "CRITICAL" or "ERROR" logs appear
* `notify2` used with fallback to console alerts
* Customize actions for future (Slack, Email, SMS)

---

## 🐳 Kafka with Docker Compose

Easiest way to run Kafka locally:

* Services: Kafka + Zookeeper (+ Kafka UI optional)
* Full `docker-compose.yml` included
* Bonus: Kafka UI for monitoring topics visually

---

## ☁️ Kafka on Confluent Cloud / AWS MSK

### ✅ Confluent Cloud

* Fully managed Kafka-as-a-Service
* Easily integrate Python clients
* Secure with API Keys

### ✅ AWS MSK

* Managed Kafka cluster inside AWS VPC
* Best for large-scale AWS-native workloads
* Python code works with minor network setup

---

## 🧠 Advanced Kafka

* **Kafka Streams** — stream processing within Kafka
* **Kafka Connect** — integration with external data sources
* **Schema Registry & Avro** — enforce data schemas
* **Monitoring** — JMX, Kafka UI, Confluent Control Center
* **Security** — SSL, SASL, ACL, encryption

---

## 🔚 Conclusion

This project is a complete Kafka ecosystem guide for Python developers. By following this journey, you’ve:

✅ Learned Kafka architecture

✅ Built Python-based Kafka apps

✅ Visualized streaming data

✅ Integrated notifications

✅ Understood production deployment strategies

---

## 📁 Project Structure

```
├── docker-compose.yml
├── producer.py
├── consumer.py
├── kafka_streamlit_ui.py
├── log_notifier.py
├── README.md
├── kafka_start.sh
└── logs/
```

---

## 💡 Next Steps

* Add REST Proxy to expose Kafka via APIs
* Use Kafka Connect to stream from databases
* Deploy real-time dashboards with Grafana
* Host on Kubernetes or cloud services

---

## 📬 Questions or Contributions?

Feel free to raise issues or submit PRs. Happy Kafka-ing! 🧡

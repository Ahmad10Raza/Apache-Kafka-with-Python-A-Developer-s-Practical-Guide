#!/bin/bash

# Config
KAFKA_VERSION="3.9.1"
SCALA_VERSION="2.13"
KAFKA_DIR="kafka_${SCALA_VERSION}-${KAFKA_VERSION}"
KAFKA_TGZ="${KAFKA_DIR}.tgz"
KAFKA_URL="https://downloads.apache.org/kafka/${KAFKA_VERSION}/${KAFKA_TGZ}"
TOPIC_NAME="logs"
VENV_NAME="kafka-env"

echo "📦 Setting up Real-Time Log Processor with Kafka..."

# 1. System Updates & Dependencies
echo "🔧 Installing system packages..."
sudo apt update
sudo apt install -y wget tar python3-dbus libdbus-glib-1-dev python3-venv openjdk-11-jdk gnome-terminal

# 2. Python Environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv "$VENV_NAME"
source "$VENV_NAME/bin/activate"

# 3. Install Python packages
echo "📚 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Download Kafka
if [ ! -d "$KAFKA_DIR" ]; then
  echo "⬇️ Downloading Kafka..."
  wget "$KAFKA_URL"
  tar -xzf "$KAFKA_TGZ"
  rm "$KAFKA_TGZ"
else
  echo "✅ Kafka already set up."
fi

# 5. Start Zookeeper
echo "🚀 Starting Zookeeper..."
gnome-terminal -- bash -c "./$KAFKA_DIR/bin/zookeeper-server-start.sh ./$KAFKA_DIR/config/zookeeper.properties; exec bash"
sleep 5

# 6. Start Kafka Broker
echo "🚀 Starting Kafka Broker..."
gnome-terminal -- bash -c "./$KAFKA_DIR/bin/kafka-server-start.sh ./$KAFKA_DIR/config/server.properties; exec bash"
sleep 8

# 7. Create Topic
echo "📡 Creating Kafka topic: $TOPIC_NAME"
./$KAFKA_DIR/bin/kafka-topics.sh --create --topic "$TOPIC_NAME" --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# 8. Start Python Producer
echo "📝 Starting Python Producer (logs to Kafka)..."
gnome-terminal -- bash -c "source $VENV_NAME/bin/activate && python3 producer.py; exec bash"

# 9. Start Python Consumer
echo "📥 Starting Python Consumer (read logs)..."
gnome-terminal -- bash -c "source $VENV_NAME/bin/activate && python3 consumer.py; exec bash"

echo "🎉 Kafka Real-Time Log Processor is now running!"

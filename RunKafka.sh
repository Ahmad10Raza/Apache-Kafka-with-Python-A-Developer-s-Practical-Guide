#!/bin/bash

# Set Kafka home directory
KAFKA_DIR=~/kafka_2.13-3.9.1

# Start Zookeeper
gnome-terminal -- bash -c "$KAFKA_DIR/bin/zookeeper-server-start.sh $KAFKA_DIR/config/zookeeper.properties; exec bash"

# Wait a few seconds for Zookeeper to initialize
sleep 5

# Start Kafka Broker
gnome-terminal -- bash -c "$KAFKA_DIR/bin/kafka-server-start.sh $KAFKA_DIR/config/server.properties; exec bash"

echo "✅ Zookeeper and Kafka Broker started in separate terminals."

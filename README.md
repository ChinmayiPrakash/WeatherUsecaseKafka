# WeatherUsecaseKafka
# **Kafka Weather Data Streaming Pipeline**

This project demonstrates a real-time streaming pipeline using Kafka to read weather data from a CSV file, publish it to a Kafka topic, and store it in a MySQL database.

---

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Install Dependencies](#step-1-install-dependencies)
  - [Step 2: Start Kafka and Zookeeper](#step-2-start-kafka-and-zookeeper)
  - [Step 3: Set Up MySQL Database](#step-3-set-up-mysql-database)
  - [Step 4: Run the Kafka Producer](#step-4-run-the-kafka-producer)
  - [Step 5: Run the Kafka Consumer](#step-5-run-the-kafka-consumer)
- [Sample Output](#sample-output)
- [Troubleshooting](#troubleshooting)
- [Security Note](#security-note)

---

## **Prerequisites**

- **Python:** 3.x  
- **Kafka Server:** Running locally  
- **MySQL Server:** Installed locally  
- **Python Dependencies:** Install using the following command:
  ```bash
  pip install kafka-python pandas mysql-connector-python

## **Creating a Kafka Topic**

### **Step 1: Navigate to Kafka Directory**

Ensure you are in the Kafka installation directory. This is where the `bin` folder and other Kafka files are located.

### **Step 2: Create a Kafka Topic**

To create a topic, run the following command:
```bash
bin/kafka-topics.sh --create --topic <topic_name> --bootstrap-server localhost:9092 --partitions <number_of_partitions> --replication-factor <replication_factor>
```

- `<topic_name>`: Specify the name of your topic (e.g., `Weather`).
- `<number_of_partitions>`: Define how many partitions you want for the topic. For example, `1` partition.
- `<replication_factor>`: This defines how many replicas of each partition are maintained. Typically set to `1` in single-node setups.

Example:
```bash
bin/kafka-topics.sh --create --topic Weather --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
This will create a topic named `Weather` with 1 partition and a replication factor of 1.

### **Step 3: Verify Topic Creation**

After creating the topic, you can verify that it exists by listing all available topics:
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

## **Setup Instructions**
### **Step 1: Install Dependencies**

Ensure that Python 3.x is installed on your system. Install the required Python packages using the following command:
- kafka-python
- pandas
- mysql-connector-python

---

### **Step 2: Start Kafka and Zookeeper**

1. Navigate to the Kafka installation directory.
2. Start the Zookeeper service.
  ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
```
4. Start the Kafka service.
```bash
   bin/kafka-server-start.sh config/server.propertie
```

---

### **Step 3: Set Up MySQL Database**

1. Connect to your MySQL server using a tool like MySQL Workbench or the terminal.
2. Create a database named `weather`.
3. Create a table `weatherdata` with the following columns:
   - `Location`: VARCHAR(50)
   - `Date_Time`: DATETIME
   - `Temperature_C`: FLOAT
   - `Humidity_pct`: FLOAT
   - `Precipitation_mm`: FLOAT
   - `Wind_Speed_kmh`: FLOAT
```bash
CREATE DATABASE weather;

USE weather;

CREATE TABLE weatherdata (
    Location VARCHAR(50),
    Date_Time DATETIME,
    Temperature_C FLOAT,
    Humidity_pct FLOAT,
    Precipitation_mm FLOAT,
    Wind_Speed_kmh FLOAT
);
```
---

### **Step 4: Run the Kafka Producer**

The Kafka producer reads the `weather_data.csv` file and streams data to the Kafka topic `Weather`.
```bash
python weatherproducer.py
```
- The producer sends data to Kafka in the following format:
  - Location, Date_Time, Temperature_C, Humidity_pct, Precipitation_mm, Wind_Speed_kmh

---

### **Step 5: Run the Kafka Consumer**

The Kafka consumer reads messages from the topic and inserts the data into the MySQL database.
```bash
python weatherconsumer.py
```
- The consumer parses the data and inserts it into the `weatherdata` table.

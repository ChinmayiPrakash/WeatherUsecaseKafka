
# **Weather Data Streamer**

## **Overview**
The Weather Data Streamer simulates the streaming of weather data to a Kafka topic, where it can be consumed and inserted into a MySQL database. The system consists of two main components:
1. **Kafka Producer**: Streams weather data from a CSV file to a Kafka topic.
2. **Kafka Consumer**: Reads the weather data from Kafka and inserts it into a MySQL database for storage and further analysis.

The weather data includes details such as temperature, humidity, precipitation, and wind speed, collected at various locations and times. This use case demonstrates the real-time transmission of weather data from producer to consumer, with integration into a database.

---

## **Kafka Producer - Data Streaming**

### **Functionality**
The producer reads weather data from a CSV file and streams it to the Kafka topic `Weather`. Each data entry contains:
- **Location**: The geographical location where the weather data was collected.
- **Date and Time**: The timestamp indicating when the weather data was recorded.
- **Temperature**: The temperature in degrees Celsius.
- **Humidity**: The humidity level as a percentage.
- **Precipitation**: The amount of precipitation in millimeters.
- **Wind Speed**: The speed of the wind in kilometers per hour.

The producer iterates through each row in the CSV file and constructs a message with the weather data. Each message is sent to Kafka as a byte-encoded string. The producer ensures data is sent in real-time, with random sleep intervals between each message to simulate real-time streaming.

---

## **Kafka Consumer - Data Processing**

### **Functionality**
The consumer reads weather data from the `Weather` Kafka topic and processes it in the following manner:
- **Message Extraction**: The consumer extracts the weather details from each Kafka message, which is a comma-separated string.
- **Data Transformation**: The consumer ensures the data is in the correct format for insertion into the database, including parsing and transforming the timestamp.
- **Database Insertion**: The consumer inserts the weather data into the MySQL database table `weatherdata`. The table stores:
  - **Location**: The location of the weather data.
  - **Date and Time**: The timestamp of the weather data.
  - **Temperature**: The temperature at the given time.
  - **Humidity**: The humidity level.
  - **Precipitation**: The amount of precipitation.
  - **Wind Speed**: The wind speed at the time of recording.

After inserting the data into the database, the consumer commits the transaction to ensure data is stored properly.

---

## **Database Interaction**

The MySQL database is set up with a table named `weatherdata` to store the weather data. The schema of the table is as follows:
- **Location**: A string representing the location of the weather observation.
- **Date and Time**: A datetime field storing when the data was recorded.
- **Temperature**: A float representing the temperature in degrees Celsius.
- **Humidity**: A float representing the humidity level as a percentage.
- **Precipitation**: A float representing the precipitation in millimeters.
- **Wind Speed**: A float representing the wind speed in kilometers per hour.

The consumer continuously reads weather data from Kafka and inserts it into the `weatherdata` table, ensuring the data is kept up-to-date.

---

## **Key Features**
- **CSV to Kafka Streaming**: The producer reads weather data from a CSV file and streams it to Kafka.
- **Real-Time Data Transmission**: The consumer processes messages in real-time as they are received from the Kafka topic.
- **Database Integration**: Weather data is stored in a MySQL database for easy retrieval and analysis.

---

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Install Dependencies](#step-1-install-dependencies)
  - [Step 2: Start Kafka and Zookeeper](#step-2-start-kafka-and-zookeeper)
  - [Step 3: Set Up MySQL Database](#step-3-set-up-mysql-database)
  - [Step 4: Run the Kafka Producer](#step-4-run-the-kafka-producer)
  - [Step 5: Run the Kafka Consumer](#step-5-run-the-kafka-consumer)


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

from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector
from mysql.connector import Error

TOPIC = 'Weather'
DATABASE = 'weather'
USERNAME = '*******'
PASSWORD = '*******'

print("Connecting to the database")

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD
    )
    
    if connection.is_connected():
        print("Connected to database")
        cursor = connection.cursor()
    else:
        print("Failed to connect to the database.")
except Error as e:
    #print(f"Error connecting to database: {e}")
    print(f"Connecting to database: {DATABASE} as user: {USERNAME}")
    exit(1)  # Exit if unable to connect to the database

print("Connecting to Kafka")

consumer = KafkaConsumer(TOPIC,
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')

try:
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=['localhost:9092'],  # Update with your Kafka server address
        auto_offset_reset='earliest',
        group_id='my-group'
    )
    print("Connected to Kafka")
    print(f"Reading messages from the topic {TOPIC}")

    for msg in consumer:
        try:
            # Extract information from Kafka message
            message = msg.value.decode("utf-8")
            Location, Date_Time, Temperature_C, Humidity_pct, Precipitation_mm, Wind_Speed_kmh = message.split(",")

         
            # Loading data into the database table
            sql = "INSERT INTO weatherdata (Location, Date_Time, Temperature_C, Humidity_pct, Precipitation_mm, Wind_Speed_kmh) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Location, Date_Time, Temperature_C, Humidity_pct, Precipitation_mm, Wind_Speed_kmh))
            connection.commit()
            print(f"A {Location} was inserted into the database")
        except Exception as e:
            print(f"Error processing message: {e}")

except Exception as e:
    print(f"Error connecting to Kafka: {e}")

finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")

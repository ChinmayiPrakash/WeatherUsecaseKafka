from kafka import KafkaProducer
import pandas as pd
import json
from time import sleep
from random import random

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092') 
TOPIC = 'Weather'

# Load the CSV file into a DataFrame
weatherdata = pd.read_csv('./weather_data.csv')

# Iterate over DataFrame rows
for index, row in weatherdata.iterrows():
    # Construct the message with the correct column names
    message = f"{row['Location']},{row['Date_Time']},{row['Temperature_C']},{row['Humidity_pct']},{row['Precipitation_mm']},{row['Wind_Speed_kmh']}"
    
    # Encode the message as bytearray
    message = bytearray(message.encode("utf-8"))
    
    # Print the message for debugging
    print(f"{row['Location']} weather condition is set to topic")
    
    # Send the message to Kafka topic
    producer.send(TOPIC, message)
    
    # Sleep for a random interval
    sleep(random() * 2)

# Ensure all messages are sent
producer.flush()
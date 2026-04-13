from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname="banking",
    user="postgres",
    password="****",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Kafka consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer en écoute sur le topic 'transactions'...")

# Fonction de détection de fraude intégrée
def is_suspicious(transaction):
    """
    Détecte si une transaction est suspecte
    """
    if transaction["amount"] > 10000:
        return True
    if transaction["location"] in ["Moscow", "Beijing", "Dubai"]:
        return True
    return False

# Lecture des messages Kafka
for message in consumer:
    transaction = message.value

    # Détection de fraude
    transaction["is_fraud"] = is_suspicious(transaction)

    # Insertion dans PostgreSQL
    cursor.execute("""
        INSERT INTO transactions (user_id, amount, location, transaction_type, timestamp, is_fraud)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        transaction["user_id"],
        transaction["amount"],
        transaction["location"],
        transaction["transaction_type"],
        transaction["timestamp"],
        transaction["is_fraud"]
    ))
    conn.commit()

    print(f"Transaction traitée : {transaction}")

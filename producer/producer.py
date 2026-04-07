import random
from kafka import KafkaProducer
import json
import time
from generator import generate_transaction

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    # Générer aléatoirement une transaction normale ou suspecte
    t = generate_transaction(normal=random.choice([True, True, True, False]))
    producer.send('transactions', t)
    print(f"Transaction envoyée : {t}")
    time.sleep(2)

from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# ⚠️ Remplace par l’IP publique de ton instance EC2 Kafka
KAFKA_BROKER = '16.16.25.53:9092'  # Adresse du broker Kafka

# === Données réalistes ===
merchants = ["jumia", "amazon", "carrefour", "uber", "airbnb"]
genders = ["M", "F"]
categories = ["shopping", "food", "transport", "entertainment", "health"]
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Nebraska",
          "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii"]
jobs = ["engineer", "doctor", "teacher", "nurse", "artist", "scientist",
        "developer", "manager", "sales", "marketing", "lawyer", "accountant",
        "technician", "analyst", "consultant", "designer", "writer", "researcher",
        "administrator", "executive", "director"]

# === Configuration du producteur Kafka ===
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# === Générateur de transaction ===
def generate_transaction():
    return {
        "merchant": random.choice(merchants),
        "category": random.choice(categories),
        "amt": round(random.uniform(1.0, 1000.0), 2),
        "gender": random.choice(genders),
        "state": random.choice(states),
        "lat": round(random.uniform(25.0, 49.0), 4),
        "long": round(random.uniform(-124.0, -66.0), 4),
        "city_pop": random.randint(500, 1000000),
        "job": random.choice(jobs),
        "merch_lat": round(random.uniform(25.0, 49.0), 6),
        "merch_long": round(random.uniform(-124.0, -66.0), 6),
        "trans_date_trans_time": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "age": random.randint(18, 90)
    }

# === Envoi continu ===
print("Simulateur en cours d'exécution... Appuyez sur Ctrl+C pour arrêter.")
while True:
    transaction = generate_transaction()
    print("Génération d'une nouvelle transaction :", transaction)
    # Envoi de la transaction au topic Kafka
    producer.send('transactions', value=transaction)
    print("✔️ Transaction envoyée :", transaction)
    time.sleep(3)

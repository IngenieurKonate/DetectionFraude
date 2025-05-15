from kafka import KafkaConsumer
import requests
import json

# IP publique du serveur Kafka EC2
KAFKA_BROKER = '16.16.25.53:9092'
TOPIC = 'transactions'

# URL du modèle ML (API Flask sur AWS)
ML_API_URL = 'http://13.50.13.122:5000/'  
# === Kafka Consumer Configuration ===
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='fraud-detector-group'
)

print("📡 Consommateur Kafka lancé...")

# === Boucle principale ===
for message in consumer:
    transaction = message.value
    print(f"\n📥 Transaction reçue : {transaction}")

    try:
        response = requests.post(ML_API_URL, json=transaction)
        if response.status_code == 200:
            prediction = response.json()
            print(f"✅ Réponse du modèle : {prediction}")
        else:
            print(f"❌ Erreur HTTP : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Erreur lors de l'envoi au modèle : {e}")

import random
import requests
import time
from datetime import datetime
import json

# === Configuration ===
API_URL = "http://13.50.13.122:5000/"  # URL de l'API
INTERVAL_SECONDES = 1  # Délai entre les requêtes

# === Données réalistes ===
merchants = ["jumia", "amazon", "carrefour", "uber", "airbnb"]
genders = ["M", "F"]
categories = ["shopping", "food", "transport", "entertainment", "health",]
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Nebraska",
          "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii"]
jobs = ["engineer", "doctor", "teacher", "nurse", "artist", "scientist",
        "developer", "manager", "sales", "marketing", "lawyer", "accountant",
        "technician", "analyst", "consultant", "designer", "writer", "researcher",
        "administrator", "executive", "director"]

def generate_transaction():
    transaction = {
        "merchant": random.choice(merchants),
        "category": random.choice(categories),
        "amt": round(random.uniform(1.0, 1000.0), 2),
        "gender": random.choice(genders),
        "state": random.choice(states),
        "lat": round(random.uniform(25.0, 49.0), 4),
        "long": round(random.uniform(-124.0, -66.0), 4),
        "city_pop": random.randint(500, 1000000),
        "job": random.choice(jobs),  # Utilisé comme code de métier
        "merch_lat": round(random.uniform(25.0, 49.0), 6),
        "merch_long": round(random.uniform(-124.0, -66.0), 6),
        "trans_date_trans_time": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "age": random.randint(18, 90)
    }
    return transaction

# === Boucle d'envoi automatique ===
while True:
    transaction = generate_transaction()
    try:
        response = requests.post(API_URL, json=transaction)
        print(f"Envoyé : {transaction}")
        print(f"Réponse : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur d'envoi : {e}")
    
    time.sleep(INTERVAL_SECONDES)

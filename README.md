# 🔍 Détection de Fraudes Bancaires en Temps Réel

Ce projet consiste à détecter les fraudes bancaires en temps réel à l’aide de Kafka, Python et un modèle de machine learning déployé sur AWS.

---

## Fonctionnalités principales

- Génération automatique de transactions (simulateur)
- Transmission des données en temps réel avec Apache Kafka
- Prédiction de fraude via un modèle ML (XGBoost)
- API Flask déployée sur AWS EC2
- Interfaces web pour le client et la banque

---
  ## Vidéo Demo

[![Watch the demo on LinkedIn](assets/video-preview.png)](https://www.linkedin.com/posts/bachiroukonate_dans-ce-projet-nous-avons-con%C3%A7u-un-pipeline-activity-7358574774958153728-RRN9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFDyVh8B1pnMiovpY9yK6sQB47mqcYDaftA)

 [Watch the full video on LinkedIn](https://www.linkedin.com/posts/bachiroukonate_dans-ce-projet-nous-avons-con%C3%A7u-un-pipeline-activity-7358574774958153728-RRN9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFDyVh8B1pnMiovpY9yK6sQB47mqcYDaftA)
 
## Architecture


[Simulateur] → [Kafka] → [Consommateur] → [API ML sur AWS] → [Consommateur] → [Base de données]→ [Interface Banque]


---

## Technologies utilisées

- Python
- Apache Kafka
- Flask (API)
- Machine Learning (XGBoost, Scikit-learn)
- AWS EC2
- HTML / Streamlit (pour interfaces)

---

## Organisation du projet


```plaintext
Fraud_detect/
│
├── Guide_kafka.pdf                  # Pour réprendre la configuration du cluster
├── simulateur_direct.py             # Simulateur qui envoie des données directement au modèle de Ml sans kafka
├── simulateur_kafkaProducer.py      # Simulateur de transactions qui envoie des données à kafka
├── consommateur_kafka.py            # Consommateur Kafka + appel modèle
├── backend                            # Dosier déployé sur AWS
   ├── application.py                  # API Flask du modèle
   ├── xgb2_model.joblib               # Modèle ML entraîné
   ├── index.html                      # Interface utilisateur
   ├── requirements.txt                # Dépendances Python
└── README.md                       # Ce fichier
```

---

## ⚙️ Prérequis

- Python 3.10+
- Apache Kafka installé
- Un serveur EC2 AWS avec le port 9092 ouvert (Si tu veux recommancer le déploiement)
- Le port 5000 ouvert pour l’API Flask (Si tu veux recommencer le déploiement)

---

## 🔧 Utilisation

1. Cloner le projet :
   ```bash
   git clone https://github.com/IngenieurKonate/DetectionFraude.git
   cd fraud-detection-project
   ```

2. Installer les dépendances :
   le dossier "backend" a déjà été déployé sur AWS donc vous pouvez passer à l'étape 3 directement 
   sans reprendre le déploiement.

   *NB:* Si Vous souhaitez faire votre propre déploiement vous devez créer une instance EC2 et déployer le dossier "backend"
   puis créer un cluster kafka en suivant le fichier "guide.kafka.pdf"

3. Lancer Kafka sur EC2 :
   accéder à mon instance EC2 (il faut remplacer: "c:\Users\HP\Downloads\clef-kafka-server.pem" par le chemin vers la clé)
   une copie de la clé se trouve dans mon projet en local

   ```bash
   ssh -i "c:\Users\HP\Downloads\clef-kafka-server.pem" ubuntu@16.16.25.53
   ```
   Accéder à kafka puis réactiver le server 

   ```bash
   cd kafka_2.13-4.0.0
   nohup bin/kafka-server-start.sh config/broker.properties > kafka.log 2>&1 &
   ps aux | grep kafka
   ```

4. Démarrer le simulateur :

 Dans un autre terminal en local
   ```bash
   python simulateur_kafkaProducer.py
   ```

5. Lancer le consommateur :
  Dans un autre terminal en local ou un autre ordinateur

   ```bash
   python consommateur_kafka.py
   ```

*NB:* avant de lancer le Simulateur et le consommateur, assurez-vous que vous avez bien kafka_2.13-4.0.0 installé
ainsi que les bibliothèques nécesaires à l'exécution de ces codes.


## ✅ À faire

- Sauvegarder les prédictions dans une base de données distante
- Concevoir le dashbord de la banque
- Ajouter des graphiques en temps réel dans l’interface banque


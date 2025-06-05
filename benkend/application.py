from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
import os

# Fonction utilitaire pour le prétraitement
def preprocess_input(input_data):
    df = pd.DataFrame([input_data])
     # Vérifier les colonnes et les transformer
    df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])
    df['hour'] = df['trans_date_trans_time'].dt.hour
    df['day_of_week'] = df['trans_date_trans_time'].dt.dayofweek
    df['day'] = df['trans_date_trans_time'].dt.day
    df['month'] = df['trans_date_trans_time'].dt.month
    df = df.drop('trans_date_trans_time', axis=1)

    #Déplacer la colonne age à la fin
    age_col = df.pop('age')
    df['age'] = age_col

    # Encoder les colonnes les variables de type object
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    print("DataFrame après transformation de la date :", )
    print(df.head())
    
    return df

# Lire le contenu du fichier HTML
def get_html_content():
    html_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        # HTML par défaut si le fichier n'existe pas
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()

# Initialisation de Flask
app = Flask(__name__)
CORS(app)  # Pour autoriser les requêtes externes

# Créer le dossier templates s'il n'existe pas
os.makedirs(os.path.join(os.path.dirname(__file__), 'templates'), exist_ok=True)

# Chargement du modèle
model = joblib.load("xgb2_model.joblib")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Servir la page HTML pour l'interface utilisateur
        return render_template_string(get_html_content())
    elif request.method == 'POST':
        try:
            # Récupérer les données JSON envoyées via POST
            data = request.get_json()

            # Vérifier que les données sont correctes
            if not data:
                return jsonify({'error': 'No input data provided'}), 400

            # Appliquer le prétraitement
            input_df = preprocess_input(data)

            # Faire la prédiction
            prediction = model.predict(input_df)

            # Retourner la prédiction sous forme JSON
            return jsonify({'prediction': int(prediction[0])})

        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Écrire le HTML dans un fichier pour être utilisé par Flask
    try: 
        f.write(get_html_content())
    except Exception as e:
        print(f"Attention: Impossible d'écrire le fichier HTML: {e}")
    
    app.run(debug=True)
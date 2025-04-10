import requests

import requests

endpoint = "http://127.0.0.1:8001/product/"

payload = {
    "name": "pomme",
    "content": "juste pomme",
    "price": 20  # 👈 nombre complexe
}

# Vérification avant d'envoyer
if isinstance(payload["price"], complex):
    print("❌ Erreur : le champ 'price' ne doit pas être un nombre complexe.")
else:
    responses = requests.post(endpoint, json=payload)
    print("✅ Statut:", responses.status_code)
    print("📦 Réponse:", responses.json())



## HTTP Resquest renvoie les données sous forme de html. dans ce cas ce n'est plus une api. Par ce qu'une api doit renvoyer le json ou le xml sinon c'est une requette http
# RESR API HTTP ----> JSON JAVASCRIPT OBJECT NOTATION
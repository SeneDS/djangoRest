import requests

import requests

endpoint = "http://127.0.0.1:8001/product/create/"

payload = {
    "name": "farine",
    "content": "",
    "price": 5  # 👈 nombre complexe
}

# Vérification avant d'envoyer
if isinstance(payload["price"], complex):
    print("❌ Erreur : le champ 'price' ne doit pas être un nombre complexe.")
else:
    responses = requests.post(endpoint, json=payload)
    print("✅ Statut:", responses.status_code)
    print("📦 Réponse:", responses.json())

import requests
endpoint = "http://127.0.0.1:8001/product/list/"
responses = requests.get(endpoint)
print("✅ Statut:", responses.status_code)
print("📦 Réponse:", responses.json())
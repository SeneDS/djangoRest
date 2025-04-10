import requests


pk = input("Entrez le nom l'id du produit que vous voulez supprimer : ")
endpoint = f"http://127.0.0.1:8001/product/{pk}/delete/"

responses = requests.delete(endpoint)
print("✅ Statut:", responses.status_code ==204)